import json
import os

MOVIES_PATH = os.path.join("data", "movies.json")

def auto_heal_movies_json():
    try:
        with open(MOVIES_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Case 1: Already correct format
        if isinstance(data, dict) and "movies" in data and isinstance(data["movies"], list):
            return  # No healing needed

        # Case 2: Nested list like [[ {...}, {...} ]]
        if isinstance(data, list) and len(data) == 1 and isinstance(data[0], list):
            healed = { "movies": data[0] }
        # Case 3: Flat list like [ {...}, {...} ]
        elif isinstance(data, list):
            healed = { "movies": data }
        else:
            raise ValueError("Unrecognized format in movies.json")

        # Overwrite with healed structure
        with open(MOVIES_PATH, "w", encoding="utf-8") as f:
            json.dump(healed, f, indent=2, ensure_ascii=False)
        print("✅ movies.json healed successfully.")

    except Exception as e:
        print(f"❌ Failed to heal movies.json: {e}")
