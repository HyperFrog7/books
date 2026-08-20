import json
import re

with open("gn-math.json", "r", encoding="utf-8") as f:
    original_data = json.load(f)

transformed_data = []

for item in original_data:
    item_id = str(item.get("id", ""))

    cover_match = re.search(r"\/([^\/]+)$", item.get("cover", ""))
    filename = cover_match.group(1) if cover_match else f"{item_id}.png"

    new_entry = {
        "name": item.get("name", ""),
        "icon": f"assets/media/icons/gn-math/{filename}",
        "file": f"gn-math/{item_id}.html"
    }

    transformed_data.append(new_entry)

with open("converted_gn-math.json", "w", encoding="utf-8") as f:
    json.dump(transformed_data, f, indent=2)

print("Conversion complete! Output saved to converted_gn-math.json")
