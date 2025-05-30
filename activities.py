from character import skill_level_up
import random as r
# <--- Random Number Roller Function --->
def rand_num():
    chance = r.randint(1, 10)
    return chance

# <--- Fishing Function --->
def skill_action(character, select_skill, skills, inventory):
    skill = skills[select_skill]
    chance = rand_num()
    # gives a 10% chance of catching a Golden Fish
    if chance % 7 == 0:
        if "golden fish" in inventory:
            inventory["golden fish"]["quantity"] += 1
        else:
            # If it's first time seeing item, add to inventory.
            inventory["golden fish"] = {"quantity": 1, "category": "valuable"}
        # Increase skill progress every successful catch
        skill["progress"] += 1
        print("Golden Fish Caught!")
        # Skill Level up check
        skill_level_up(character, skill)
    elif chance % 3 == 0:
        inventory["fish"]["quantity"] += 1
        # Increase skill progress every successful catch
        skill["progress"] += 1
        print("Fish Caught!")
        # Skill Level up check
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
            # If it's first time seeing item, add to inventory.
            inventory["ancient log"] = {"quantity": 1, "category": "crafting"}
        # Increase skill progress every successful chop
        skill["progress"] += 1
        print("Ancient Log Found!")
        # Skill Level up check
        skill_level_up(character, skill)
    elif chance % 3 == 0:
        inventory["log"]["quantity"] += 1
        # Increase skill progress every successful chop
        skill["progress"] += 1
        print("Log found!")
        # Skill Level up check
        skill_level_up(character, skill)
    else:
        print("...")