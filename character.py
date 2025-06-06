import util as j
from pathlib import Path

savegames = Path("data/savegames/save_file.json")

# <--- Initial Game Load --->
def current_character():
    load_save = input("Load saved character(y/n): ")
    # Keep prompting if invalid answer
    while True:
        # Continue from last saved character
        if load_save == "y":
            character = j.load_file(savegames)
            print(f"Welcome back to Skill Town {character['name']}")
            return character
        # Start a new character
        elif load_save == "n":
            character = new_character_setup()
            print(f"Welcome to Skill Town {character['name']}")
            return character
        # If user makes typo
        else:
            print(f"{load_save} is not an Option!")

# <--- Setting Up a New Character --->
def new_character_setup():
    # Store entered name in a variable to add to dictionary
    player_name = input("Enter Name: ")
    # Offer the player a starting skill of either Woodcutting or Fishing
    print(f"Welcome {player_name}!\nYou may choose either Woodcutting or Fishing for your starting skill")
    # Keep prompting if invalid answer
    while True:
        choose_starting_skill = input("Starting skill (w/f): ").lower()
        # Store their choice in a variable to add to character dictionary
        if choose_starting_skill == "w":
            starting_skill = "woodcutting"
            starting_tool = "axe"
            starting_item = "log"
            break
        elif choose_starting_skill == "f":
            starting_skill = "fishing"
            starting_tool = "fishing rod"
            starting_item = "fish"
            break
        else:
            print("Invalid Option, Stating skills are \n - (w) Woodcutting \n - (f) Fishing")

    # <--- New Character Creation --->
    # Populate initial character dictionary with defaults
    new_character = {
        # Stored from user input
        "name": player_name,
        "skills": {
            # Stored from user input
            starting_skill: {
                "level": 0,
                "progress": 0
            }
        },
        "strength": 10,
        "stamina": 50,
        "luck": 0,
        # Populate character inventory based on their chosen starting skill
        "inventory": {
            starting_tool: 1,
            starting_item: 0
        }
    }

    # Display their chosen Name, starting skill and initial inventory
    print(f"Character Created {player_name}, you start off with a {starting_tool} and "
          f"knowledge of {starting_skill}")
    for item, qty in new_character["inventory"].items():
        print(f"{item}: {qty}")
    # Return new character dictionary to main
    return new_character

# <--- Skill Level Up Checker --->
def skill_level_up(character, skill):
    if skill["progress"] >= 5:
        character["strength"] += 1
        skill["level"] += 1
        skill["progress"] = 0
        print(f"{skill} now level {skill["level"] }")

# <--- Consume Item Function --->
def use_consumable(character, inventory):
    use_item = input("Use Item: ")
    if use_item in inventory.keys():
        item = inventory[use_item]
        effect = item["effect"]
        value = item["effect value"]
        item["quantity"] -= 1
        if effect == "stamina boost":
            character["stamina"] += value
            print(f"Stamina increased by {value} points")
            return
    else:
        print(f"{use_item} not found in inventory")
