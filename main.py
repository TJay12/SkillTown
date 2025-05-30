from character import new_character_setup, save_character, load_saved_character, use_consumable
import activities

load_save = input("Load saved character(y/n): ")
while True:
    if load_save == "y":
        character = load_saved_character()
        print(f"Welcome back to Skill Town {character['name']}")
        break
    elif load_save == "n":
        character = new_character_setup()
        print(f"Welcome to Skill Town {character['name']}")
        break
    else:
        print(f"{load_save} is not an Option!")

name = character["name"]
skills = character["skills"]
inventory = character["inventory"]

while True:
    print(f"(S)kill Activity, (C)haracter Stats, (I)nventory, (U)se Item (Q)uit")
    action = input("Action: ").lower()
    if action == "s":
        for skill in skills:
            lvl = skills[skill]["level"]
            print(f"{skill} level {lvl}")
        select_skill = input("Which Activity: ").lower()
        if select_skill == "fishing":
            print("Fishing ...")
            while True:
                activities.fishing(character, skills, inventory)

                back = input("(B)ack ").lower()
                if back == "b":
                    break
        elif select_skill == "woodcutting":
            print("Woodcutting")
            while True:
                activities.woodcutting(character, skills, inventory)
                back = input("(B)ack ").lower()
                if back == "b":
                    break
    elif action == "c":
        print(f"{name}'s Current Stats:")
        for stat, value in character.items():
            if stat != "inventory" and stat != "skills":
                print(f" - {stat} : {value}")
        print("\nSkills:")
        for skill in skills:
            lvl = skills[skill]["level"]
            print(f" - {skill} level {lvl}")

    elif action == "i":
        for item in character["inventory"].keys():
            qty = character["inventory"][item]["quantity"]
            print(f"{item} : {qty}")

    elif action == "u":
        print("Useable Items:")
        for item in character["inventory"].keys():
            if character["inventory"][item]["category"] == "consumable":
                print(f" - {item}")
            consume = use_consumable(character)

    elif action == "q":
        save = input("Save Character(y/n): ")
        if save == "y":
            save_character(character)
            print(f"{character['name'].title()} has been saved. See you next time!")
            break
        else:
            break
