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


    def get_item_name(self):
        return self.name

    def get_item_effect(self):
        return self.item_effect

    def disable_trap(self):
        message = "Using the {} you successfully disabled the trap".format(self.name)
        print(message)

    # gets data_gain attribute for when player uses a healing item.
    def get_data_gain(self):
        return self.data_gain

    # fetches name
    def get_name(self):
        return self.name

    def can_be_used(self):
        if self.can_scan or self.data_gain > 0:
            return True

        return False

    def is_a_scan_item(self):
        return self.can_scan


