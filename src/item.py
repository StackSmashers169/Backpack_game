# code written by Victor J Wilson

# the item class, each item has a name and default count value of 1.
class Item:

    def __init__(self, name: str, item_effect: str, data_gain: int):
        self.name = name
        self.count = 1
        self.item_effect = item_effect
        self.data_gain = data_gain

    # displays effect on console
    def read_effect(self):
        pass

    def disable_trap(self):
        pass


