from character import skill_level_up
import random as r
def rand_num():
    chance = r.randint(1, 10)
    return chance


# <--- Fishing Function --->
def fishing(character):
    chance = rand_num()
    if chance % 7 == 0:
        if "golden fish" in character["inventory"]:
            character["inventory"]["golden fish"]["quantity"] += 1
        else:
            character["inventory"]["golden fish"] = {"quantity": 1, "category": "valuable"}
        character["skill progress"] += 1
        print("Golden Fish Caught!")
        skill_level_up(character)
    elif chance % 2 == 0:
        character["inventory"]["fish"]["quantity"] += 1
        character["skill progress"] += 1
        print("Fish Caught!")
        skill_level_up(character)
    else:
        print("...")

# <--- Woodcutting Function --->
def woodcutting(character):
    chance = rand_num()
    if chance % 7 == 0:
        if "ancient log" in character["inventory"]:
            character["inventory"]["ancient log"]["quantity"] += 1
        else:
            character["inventory"]["ancient log"] = {"quantity": 1, "category": "crafting"}
        character["skill progress"] += 1
        print("Ancient Log Found!")
        skill_level_up(character)
    elif chance % 2 == 0:
        character["inventory"]["log"]["quantity"] += 1
        character["skill progress"] += 1
        print("Log found!")
        skill_level_up(character)
    else:
        print("...")