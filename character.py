import json
# <--- User Input Initiation --->
def new_character_setup():
    player_name = input("Enter Name: ")
    print(f"Welcome {player_name}!\nYou may choose either Woodcutting or Fishing for your starting skill")
    while True:
        choose_starting_skill = input("Starting skill (w/f): ").lower()
        if choose_starting_skill == "w":
            starting_skill = "woodcutting"
            break
        elif choose_starting_skill == "f":
            starting_skill = "fishing"
            break
        else:
            print("Invalid Option, Stating skills are \n - (w) Woodcutting \n - (f) Fishing")

    # <--- New Character Creation --->
    new_character = {
        "name": player_name,
        "skill": starting_skill,
        "skill level": 0,
        "skill progress": 0,
        "strength": 10,
        "stamina": 50,
        "luck": 0,
        "inventory": {}
    }

    if new_character["skill"] == "woodcutting":
        new_character["inventory"]["log"] = {"quantity": 0, "category": "crafting"}
    elif new_character["skill"] == "fishing":
        new_character["inventory"]["fish"] = {"quantity": 0, "category": "consumable",
                                              "effect": "stamina boost", "effect value": 10}

    print(f"Character Created {player_name}, you start off {starting_skill}")
    for item in new_character["inventory"].keys():
        qty = new_character["inventory"][item]["quantity"]
        print(item, qty)

    return new_character

def skill_level_up(character):
    if character["skill progress"] >= 5:
        character["strength"] += 1
        character["skill level"] += 1
        character["skill progress"] = 0
        print(f"{character['skill']} now level {character["skill level"]}")

def save_character(character):
    with open("data/save_file.json", "w") as file:
        data = character
        json.dump(data, file, indent=2)

def load_saved_character():
    with open("data/save_file.json", "r") as file:
        character = json.load(file)
        return character

def use_consumable(character):
    use_item = input("Use Item: ")
    if use_item in character["inventory"].keys():
        item = character["inventory"][use_item]
        effect = item["effect"]
        value = item["effect value"]
        item["quantity"] -= 1
        if effect == "stamina boost":
            character["stamina"] += value
            print(f"Stamina increased by {value} points")
            return
    else:
        print(f"{use_item} not found in inventory")


