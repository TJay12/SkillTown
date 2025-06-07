import util as j
from pathlib import Path

savegames = Path("data/savegames/save_file.json")
skills = Path("data/skills.json")
main_items = Path("data/main_items.json")
special_items = Path("data/special_items.json")
crafting = Path("data/crafting_recipies.json")

# <--- Add Entry To Skills File --->
def add_to_skills():
    path = skills
    data = j.load_file(path)

    skill_name = input("Skill Name: ").lower()
    tool = input("Tool: ").lower()
    stamina_cost = input("Stamina Cost: ").lower()
    main_item = input("Main Item: ").lower()
    special_item = input("Special Item: ").lower()
    skill_info = {"tool": tool, "stamina cost": stamina_cost, "main item": main_item,
                  "special item": special_item}
    data[skill_name] = skill_info

    j.save_file(path, data)
    print(f"{skill_name} added to {path}")

# <--- Add Entry To Items Files --->
def add_to_main_items():
    path = main_items
    data = j.load_file(path)

    item_key = input("Item: ").lower()
    category = input("Category: ").lower()
    effect = input("Special Effect: ").lower()
    effect_value = input("Special Effect Value: ").lower()
    value = input("Value: ").lower()
    item_info = {"category": category, "effect": effect,
                 "effect value": effect_value, "value": value}
    data[item_key] = item_info

    j.save_file(path, data)
    print(f"{item_key} added to {path}")

def add_to_special_items():
    path = special_items
    data = j.load_file(path)

    item_key = input("Item: ").lower()
    category = input("Category: ").lower()
    effect = input("Special Effect: ").lower()
    effect_value = input("Special Effect Value: ").lower()
    value = input("Value: ").lower()
    item_info = {"category": category, "effect": effect,
                 "effect value": effect_value, "value": value}
    data[item_key] = item_info

    j.save_file(path, data)
    print(f"{item_key} added to {path}")

# <--- Add Entry To Crafting File--->
def add_to_crafting():
    path = crafting
    data = j.load_file(path)

    recipe_name = input("Recipe Name: ").lower()
    comp1 = input("Component 1: ").lower()
    comp1_qty = input("Component 1 Quantity: ").lower()
    comp2 = input("Component 2: ").lower()
    comp2_qty = input("Component 2 Quantity: ").lower()
    value = {comp1: comp1_qty, comp2: comp2_qty}
    data[recipe_name] = value

    j.save_file(path, data)
    print(f"{recipe_name} added to {path}")

# add_to_skills()
# add_to_main_items()
# add_to_special_items()
# add_to_crafting()