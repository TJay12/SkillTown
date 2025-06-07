# <--- Imports --->
from classes.Skills import Skill
import util as j
from pathlib import Path

# <--- Data Paths --->
savegames = Path("data/savegames/save_file.json")
skills = Path("data/skills.json")
main_items = Path("data/main_items.json")
special_items = Path("data/special_items.json")
crafting = Path("data/crafting_recipies.json")

# <--- Add Quantity of Item(s) to Player Inventory --->
def add_to_inventory(inventory, item, qty):
    if "nothing found" in item:
        return
    item_name = item.replace(" found", "")
    if item_name in inventory:
        inventory[item_name] += qty
    else:
        inventory[item_name] = qty
    print(f"{item_name} + {qty}")

# <--- Perform chosen skill action from menu
def perform_skill(inventory):
    # Store player selected skill in variable
    select_skill = input("Which Activity: ").lower().capitalize()
    # Skill Data
    data = j.load_file(skills)
    print(f"Selected Skill: {select_skill}")
    if select_skill in data:
        skill = data[select_skill]
        skill_tool = skill['tool']
        skill_stam = skill['stamina cost']
        skill_main_item = skill['main item']
        skill_spec_item = skill['special item']
    else:
        print("Skill not found")
        return
    # Run skill action function until player exits
    print(f"{select_skill} ...")
    select_skill = Skill(
        name=select_skill,
        tool=skill_tool,
        stam_cost=skill_stam,
        main_item=skill_main_item,
        special_item=skill_spec_item

        )
    while True:
        item = select_skill.action()
        add_to_inventory(inventory, item, qty=1)
        # Option to exit
        back = input("(B)ack ").lower()
        if back == "b":
            break
