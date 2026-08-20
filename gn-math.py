import json
import os

INPUT_FILE = "gn-math.json"
OUTPUT_FILE = "formatted_gn-math.json"
ICONS_DIR = "media/icons/gn-math"
GAMES_DIR = "games"


def convert_gnmath():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found.")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        try:
            gnmath_data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error reading {INPUT_FILE}: {e}")
            return

    new_data = []

    for item in gnmath_data:
        title = (item.get("name") or item.get("title") or "").strip()
        raw_icon = item.get("icon") or item.get("image") or ""
        raw_file = item.get("file") or item.get("url") or item.get("path") or ""

        icon_filename = os.path.basename(raw_icon) if raw_icon else ""
        file_filename = os.path.basename(raw_file) if raw_file else ""

        entry = {
            "name": title,
            "icon": (
                f"{ICONS_DIR}/{icon_filename}" if icon_filename else ""
            ),
            "file": (
                f"{GAMES_DIR}/{file_filename}" if file_filename else ""
            ),
        }

        new_data.append(entry)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(new_data, f, indent=2)

    print(f"Done! Created {OUTPUT_FILE} with {len(new_data)} items.")


if __name__ == "__main__":
    convert_gnmath()
