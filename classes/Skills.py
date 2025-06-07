from util import rand_num

class Skill:
    def __init__(self, name, tool, stam_cost, main_item, special_item):
        self.name = name
        self.tool = tool
        self.stam_cost = stam_cost
        self.main_item = main_item
        self.special_item = special_item

    def action(self):
        chance = rand_num()
        # gives a 10% chance of catching a Special Item
        if chance % 7 == 0:
            item = self.special_item + " found"
        # gives a 30% chance of catching a Main Item
        elif chance % 3 == 0:
            item = self.main_item + " found"
        else:
            item = "nothing found"
        print(item)
        return item