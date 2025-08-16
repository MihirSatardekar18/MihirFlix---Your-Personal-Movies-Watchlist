import os, json, time, webbrowser, datetime as dt
from typing import List, Dict, Any

MOVIES_FILE = "data/movies.json"
POSTERS_DIR = "assets/posters"

def ensure_dirs():
    os.makedirs(os.path.dirname(MOVIES_FILE), exist_ok=True)
    os.makedirs(POSTERS_DIR, exist_ok=True)
    if not os.path.exists(MOVIES_FILE):
        with open(MOVIES_FILE, "w", encoding="utf-8") as f:
            json.dump({"movies": []}, f, ensure_ascii=False, indent=2)

def load_movies() -> List[Dict[str, Any]]:
    ensure_dirs()
    try:
        with open(MOVIES_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("movies", [])
    except Exception:
        return []

def save_movies(movies: List[Dict[str, Any]]):
    ensure_dirs()
    with open(MOVIES_FILE, "w", encoding="utf-8") as f:
        json.dump({"movies": movies}, f, ensure_ascii=False, indent=2)

def list_posters() -> List[str]:
    ensure_dirs()
    files = []
    for name in sorted(os.listdir(POSTERS_DIR)):
        p = os.path.join(POSTERS_DIR, name)
        if os.path.isfile(p) and name.lower().split(".")[-1] in {"png", "jpg", "jpeg", "webp"}:
            files.append(name)
    return files

def validate_youtube(url: str) -> bool:
    u = (url or "").strip().lower()
    return ("youtube.com/watch" in u) or ("youtu.be/" in u)

def year_bounds():
    year_now = dt.datetime.now().year
    return 1878, year_now + 1

def make_movie_id() -> str:
    return f"mv_{int(time.time())}"

def title_year_exists(movies, title: str, year: int) -> bool:
    t = (title or "").strip().lower()
    for m in movies:
        if m.get("title", "").strip().lower() == t and int(m.get("year", 0)) == int(year):
            return True
    return False

def open_url(url: str):
    try:
        webbrowser.open_new_tab(url)
    except Exception:
        pass

def stars_text(rating: float) -> str:
    # Full stars only for UI simplicity
    full = int(round(rating))
    full = max(0, min(full, 5))
    return "★" * full + "☆" * (5 - full)
