# code written by Victor J Wilson

# the item class, each item has a name and default count value of 1.
class Item:

    def __init__(self, name: str, item_effect: str, data_gain: int, can_disable: bool):
        self.name = name
        self.item_effect = item_effect
        self.data_gain = data_gain
        self.can_disable = can_disable
        self.count = 1

    # displays effect on console/terminal
    def read_effect(self):
        pass

    def disable_trap(self):
        pass

    #fetches name
    def get_name(self):
        return self.name
