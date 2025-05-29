from character import new_character_setup, save_character, load_saved_character, use_consumable
import activities

load_save = input("Load saved character(y/n): ")
if load_save == "y":
    character = load_saved_character()
    skill = character["skill"]
    print(f"Welcome back to Skill Town {character['name']}")
elif load_save == "n":
    character = new_character_setup()
    skill = character["skill"]
    print(f"Welcome to Skill Town {character['name']}")

while True:
    print(f"(S)kill Activity, (C)haracter Stats, (I)nventory, (U)se Item (Q)uit")
    action = input("Action: ").lower()
    if action == "s":
        if skill == "fishing":
            print("Fishing ...")
            while True:
                activities.fishing(character)

                back = input("(B)ack").lower()
                if back == "b":
                    break
        elif skill == "woodcutting":
            print("Woodcutting")
            while True:
                activities.woodcutting(character)
                back = input("(B)ack").lower()
                if back == "b":
                    break
    elif action == "c":
        for stat, value in character.items():
            if stat != "inventory":
                print(f"{stat} : {value}")

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
