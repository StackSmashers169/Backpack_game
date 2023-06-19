# code written by Victor J Wilson

# the item class, each item has a name and default count value of 1.
class Item:

    def __init__(self, name: str, item_effect: str, data_gain: int, can_disable: bool,
                 can_scan: bool):
        self.name = name
        self.item_effect = item_effect
        self.data_gain = data_gain
        self.can_disable = can_disable
        self.can_scan = can_scan

    # displays effect on console/terminal
    def read_effect(self):
        print(self.item_effect)

    def disable_trap(self):
        message = "Using the {} you successfully disabled the trap".format(self.name)
        print(message)

    # fetches name
    def get_name(self):
        return self.name

    def gain_data(self, data: int):
        data = data + 10
        return data
