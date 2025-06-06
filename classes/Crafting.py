class Crafting:
    def __init__(self, name, component1, component1_qty, component2, component2_qty):
        self.name = name
        self.component1 = component1
        self.component1_qty = component1_qty
        self.component2 = component2
        self.component2_qty = component2_qty

    def craft(self):
        print(f"To craft {self.name} you need {self.component1_qty} {self.component1} and {self.component2_qty}"
              f"{self.component2}")