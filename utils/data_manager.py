import json
import os

# Default data file paths
MOVIES_FILE = os.path.join("data", "movies.json")
USER_STATE_FILE = os.path.join("data", "user_state.json")


def _ensure_file(path, default_data):
    """
    Agar file nahi hai to default data create karo.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(default_data, f, indent=4)


def load_movies():
    """
    Load movies.json content; agar nahi mila to empty list banado.
    """
    _ensure_file(MOVIES_FILE, [])
    with open(MOVIES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_movies(movies):
    """
    Save movies list to movies.json
    """
    os.makedirs(os.path.dirname(MOVIES_FILE), exist_ok=True)
    with open(MOVIES_FILE, "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=4)


def load_user_state(username):
    """
    Per‑user watched/favorite state load kare.
    """
    _ensure_file(USER_STATE_FILE, {})
    with open(USER_STATE_FILE, "r", encoding="utf-8") as f:
        state = json.load(f)
    return state.get(username, {})


def save_user_state(username, user_data):
    """
    Per‑user watched/favorite state save kare.
    """
    _ensure_file(USER_STATE_FILE, {})
    with open(USER_STATE_FILE, "r", encoding="utf-8") as f:
        state = json.load(f)
    state[username] = user_data
    with open(USER_STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=4)
