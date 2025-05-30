from character import skill_level_up
import random as r
def rand_num():
    chance = r.randint(1, 10)
    return chance


# <--- Fishing Function --->
def fishing(character, skills, inventory):
    skill = skills["fishing"]
    chance = rand_num()
    if chance % 7 == 0:
        if "golden fish" in inventory:
            inventory["golden fish"]["quantity"] += 1
        else:
            inventory["golden fish"] = {"quantity": 1, "category": "valuable"}
        skill["progress"] += 1
        print("Golden Fish Caught!")
        skill_level_up(character, skill)
    elif chance % 3 == 0:
        inventory["fish"]["quantity"] += 1
        skill["progress"] += 1
        print("Fish Caught!")
        skill_level_up(character, skill)
    else:
        print("...")

# <--- Woodcutting Function --->
def woodcutting(character, skills, inventory):
    skill = skills["woodcutting"]
    chance = rand_num()
    if chance % 7 == 0:
        if "ancient log" in inventory:
            inventory["ancient log"]["quantity"] += 1
        else:
            inventory["ancient log"] = {"quantity": 1, "category": "crafting"}
        skill["progress"] += 1
        print("Ancient Log Found!")
        skill_level_up(character, skill)
    elif chance % 3 == 0:
        inventory["log"]["quantity"] += 1
        skill["progress"] += 1
        print("Log found!")
        skill_level_up(character, skill)
    else:
        print("...")