import json
from pathlib import Path

savegames = Path("data/savegames")
crafting = Path("data/crafting")
items = Path("data/items")
skills = Path("data/skills")

# <--- Add Entry To Crafting File--->
def add_to_crafting():
    filename = input("Filename: ") + ".json"
    path = crafting / filename
    with path.open("r") as file:
        data = json.load(file)

        key = input("Key: ").lower()
        value = input("Value: ").lower()
        data[key] = value

    with path.open("w") as file:
        json.dump(data, file, indent=2)
    print(f"{key}: {value} added to {path}")

# <--- Add Entry To Item File --->
def add_to_items():
    filename = input("Filename: ") + ".json"
    path = items / filename
    with path.open("r") as file:
        data = json.load(file)

        key = input("Key: ").lower()
        value = input("Value: ").lower()
        data[key] = value

    with path.open("w") as file:
        json.dump(data, file, indent=2)
    print(f"{key}: {value} added to {path}")

# <--- Add Entry To Skill File --->
def add_to_skills():
    filename = input("Filename: ") + ".json"
    path = skills / filename
    with path.open("r") as file:
        data = json.load(file)

        key = input("Key: ").lower()
        value = input("Value: ").lower()
        data[key] = value

    with path.open("w") as file:
        json.dump(data, file, indent=2)
    print(f"{key}: {value} added to {path}")

# add_to_skills()
add_to_items()
# add_to_crafting()