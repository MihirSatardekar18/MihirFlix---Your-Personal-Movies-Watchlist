import json, os, webbrowser, time

# ---------- Paths ----------
DATA_DIR = "data"
MOVIES_FILE = os.path.join(DATA_DIR, "movies.json")
USERS_DIR = os.path.join(DATA_DIR, "users")
POSTERS_DIR = os.path.join("assets", "posters")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(USERS_DIR, exist_ok=True)
os.makedirs(POSTERS_DIR, exist_ok=True)

# ---------- JSON helpers ----------
def _load_json(path, default):
    if not os.path.exists(path):
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default

def _save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ---------- User state helpers ----------
def _user_file(username):
    return os.path.join(USERS_DIR, f"{username}.json")

def _get_state(username):
    state = _load_json(_user_file(username), {})
    changed = False
    if "password" not in state:
        state["password"] = ""
        changed = True
    if "watched_ids" not in state:
        state["watched_ids"] = []
        changed = True
    if "watchlist_ids" not in state:
        state["watchlist_ids"] = []
        changed = True
    if "watched_history" not in state:           # NEW for history
        state["watched_history"] = []
        changed = True
    if changed:
        _save_json(_user_file(username), state)
    return state

# ---------- Init ----------
def init_storage():
    if not os.path.exists(MOVIES_FILE):
        _save_json(MOVIES_FILE, {"movies": []})

# ---------- User management ----------
def register_user(username, password):
    path = _user_file(username)
    if os.path.exists(path):
        return False, "User already exists."
    _save_json(path, {
        "password": password,
        "watched_ids": [],
        "watchlist_ids": [],
        "watched_history": []
    })
    return True, "Registration successful."

def validate_login(username, password):
    path = _user_file(username)
    if not os.path.exists(path):
        return False, "User does not exist."
    data = _load_json(path, {})
    if data.get("password") == password:
        return True, "Login successful."
    return False, "Invalid password."

# ---------- Movie catalog ----------
def _heal_movies_format(data):
    if isinstance(data, dict) and isinstance(data.get("movies"), list):
        return data["movies"]
    if isinstance(data, list) and len(data) == 1 and isinstance(data[0], list):
        return data[0]
    if isinstance(data, list):
        return data
    return []

def get_catalog():
    raw = _load_json(MOVIES_FILE, {"movies": []})
    movies = _heal_movies_format(raw)
    healed = []
    changed = False
    for m in movies:
        if not isinstance(m, dict):
            continue
        if "poster_path" not in m:
            m["poster_path"] = ""
            changed = True
        if "trailer_url" not in m:
            m["trailer_url"] = ""
            changed = True
        healed.append(m)
    if changed:
        _save_json(MOVIES_FILE, {"movies": healed})
    return healed

def add_movie(movie: dict):
    movies = get_catalog()
    if not movie.get("id") or not movie.get("title"):
        return False, "Movie must have id and title."
    if any(m.get("id") == movie["id"] for m in movies):
        return False, "Movie already exists."
    if "poster_path" not in movie:
        movie["poster_path"] = ""
    if "trailer_url" not in movie:
        movie["trailer_url"] = ""
    movies.append(movie)
    _save_json(MOVIES_FILE, {"movies": movies})
    return True, "Movie added."

def delete_movie(movie_id: str):
    movies = get_catalog()
    new_movies = [m for m in movies if m.get("id") != movie_id]
    if len(new_movies) == len(movies):
        return False, "Movie not found."
    _save_json(MOVIES_FILE, {"movies": new_movies})
    return True, "Movie deleted."

# ---------- Watched / Watchlist ----------
def is_watched(username, movie_id):
    return movie_id in set(_get_state(username)["watched_ids"])

def mark_watched(username, movie_id):
    state = _get_state(username)
    if movie_id not in state["watched_ids"]:
        state["watched_ids"].append(movie_id)
    # Add full movie info to watched_history
    movie = next((m for m in get_catalog() if m.get("id") == movie_id), None)
    if movie:
        entry = dict(movie)
        entry["timestamp"] = time.time()
        # Remove old entry if exists
        state["watched_history"] = [m for m in state["watched_history"] if m.get("id") != movie_id]
        state["watched_history"].insert(0, entry)
        # Limit history size if needed
        state["watched_history"] = state["watched_history"][:50]
    _save_json(_user_file(username), state)

def toggle_watched(username, movie_id):
    """
    Toggle watched status.  
    If watched → unwatch (also removes from history)  
    If not watched → mark watched (and optionally remove from watchlist)
    """
    state = _get_state(username)
    if movie_id in state["watched_ids"]:
        # Unwatch
        state["watched_ids"].remove(movie_id)
        state["watched_history"] = [
            m for m in state["watched_history"] if m.get("id") != movie_id
        ]
        _save_json(_user_file(username), state)
    else:
        mark_watched(username, movie_id)
        # Premium touch: Remove from watchlist automatically when watched
        if movie_id in state["watchlist_ids"]:
            state["watchlist_ids"].remove(movie_id)
            _save_json(_user_file(username), state)

def get_recent_watched(username, limit=5):
    state = _get_state(username)
    return sorted(state.get("watched_history", []), key=lambda m: m.get("timestamp", 0), reverse=True)[:limit]

def list_watchlist_movies(username):
    ids = set(_get_state(username)["watchlist_ids"])
    return [m for m in get_catalog() if m.get("id") in ids]

def add_to_watchlist(username, movie_id):
    state = _get_state(username)
    if movie_id not in state["watchlist_ids"]:
        state["watchlist_ids"].append(movie_id)
        _save_json(_user_file(username), state)

def remove_from_watchlist(username, movie_id):
    state = _get_state(username)
    if movie_id in state["watchlist_ids"]:
        state["watchlist_ids"].remove(movie_id)
        _save_json(_user_file(username), state)

# ---------- Assets ----------
def list_poster_files():
    return [f for f in os.listdir(POSTERS_DIR)
            if os.path.isfile(os.path.join(POSTERS_DIR, f))]

def open_trailer(url):
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"Failed to open trailer: {e}")
