import json

def save_character(character):
    with open("data/save_file.json", "w") as file:
        data = character
        json.dump(data, file, indent=2)

def load_saved_character():
    with open("data/save_file.json", "r") as file:
        character = json.load(file)
        return character