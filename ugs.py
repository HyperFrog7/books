import json

INPUT_FILE = "ugs.json"
OUTPUT_FILE = "ugs.json"
PLACEHOLDER_ICON = "images/icons/placeholder.png"

def transform_json(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    formatted_data = []
    for item in data:
        formatted_entry = {
            "name": item.get("name", ""),
            "img": PLACEHOLDER_ICON,
            "file": item.get("file", "")
        }
        formatted_data.append(formatted_entry)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(formatted_data, f, indent=2)

    print(f"Successfully formatted {len(formatted_data)} items into '{output_path}'.")

if __name__ == "__main__":
    transform_json(INPUT_FILE, OUTPUT_FILE)
