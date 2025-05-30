import json
from pathlib import Path

savegames = Path("data/savegames")
crafting = Path("data/crafting")
items = Path("data/items")
skills = Path("data/skills")

def save_character(character):
    with open(savegames / "save_file.json", "w") as file:
        data = character
        json.dump(data, file, indent=2)

def load_saved_character():
    with open(savegames / "save_file.json", "r") as file:
        character = json.load(file)
        return character

def load_file(category, item):
    filename = item + ".json"
    path = category / filename
    print(path)
    with path.open("r") as file:
        data = json.load(file)
        return data
