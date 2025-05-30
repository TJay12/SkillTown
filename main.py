from character import current_character
from menus import main_menu

# <--- Main Program --->
def main():
    # Load character dictionary
    #  - either fron save file
    #  - or new character creation
    character = current_character()
    # For simplification store name and nested dictionaries in their own variables
    name = character["name"]
    skills = character["skills"]
    inventory = character["inventory"]
    # Pass these variables into main menu for ease of access from other functions
    main_menu(character, name, skills, inventory)

main()