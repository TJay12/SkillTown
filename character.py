# <--- User Input Initiation --->
def new_character_setup():
    player_name = input("Enter Name: ").lower()
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
        "strength": 10,
        "stamina": 50,
        "luck": 0,
        "inventory": {}
    }

    if new_character["skill"] == "woodcutting":
        new_character["inventory"]["log"] = 0
    elif new_character["skill"] == "fishing":
        new_character["inventory"]["fish"] = 0

    print(f"Character Created {player_name}, you start off {starting_skill}")
    for item, qty in new_character["inventory"].items():
        print(item, qty)

new_character_setup()