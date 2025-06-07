from character import use_consumable
import util as j
from pathlib import Path
import actions as a

savegame = Path("data/savegames/save_file.json")

# <--- Main Gameplay Menu --->
def main_menu(character, name, skills, inventory):
    # Loop back to options unless quit
    while True:
        # Display menu options to player
        print(f"(S)kill Activity, (C)haracter Stats, (I)nventory, "
              f"(U)se Item (Q)uit")
        # Store player choice in value
        action = input("Action: ").lower()
        # Skill Activity
        if action == "s":
            # Display available skills and their level
            for skill in skills:
                lvl = skills[skill]["level"]
                print(f"{skill} level {lvl}")
            a.perform_skill(inventory)

        # Character Stats
        elif action == "c":
            print(f"{name}'s Current Stats:")
            # Display main stats, ignore nested dicts
            for stat, value in character.items():
                if stat != "inventory" and stat != "skills":
                    print(f" - {stat} : {value}")
            # Display Skills and level from nested dict skills
            print("\nSkills:")
            for skill in skills:
                lvl = skills[skill]["level"]
                print(f" - {skill} level {lvl}")
        # Display Inventory
        elif action == "i":
            # Display inventory items and quantity from nested dict inventory
            for item, qty in inventory.items():
                print(f"{item} : {qty}")
        # Use Item From Inventory
        elif action == "u":
            print("Useable Items:")
            # Display items from inventory with consumable tag(category)
            for item in inventory.keys():
                if inventory[item]["category"] == "consumable":
                    print(f" - {item}")
                # Run use consumable function in character
                use_consumable(character, inventory)
        # Quit Game
        elif action == "q":
            # Option to save character before exiting
            save = input("Save Character(y/n): ")
            # Saves character to .json file then close
            if save == "y":
                j.save_file(savegame, character)
                print(f"{character['name'].title()} has been saved. See you next time!")
                break
            # Close without saving character (New character would have to be created on next play)
            elif save == "n":
                break
            # The classic protection against user input error
            else:
                print(f"{save} is not a valid option!")
        # The classic protection against user input error
        else:
            print(f"{action} is not a valid option!")

