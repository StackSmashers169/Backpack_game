# code written by Victor J Wilson

# the item class, each item has a name and default count value of 1.
class Item:

    def __init__(self, name: str, item_effect: str, data_gain: int, can_disable: bool,
                 can_scan: bool):
        """Attribute explanations
        name: Name of the Item
        item_effect: The item's description
        data_gain: Gives the player 'data', data is this game's version of Health Points
        can_disable: The item can nullify the effects of a trap_location
        can_scan: The item can scan a location and to get the name of the scanned location and mark it on the map"""

        self.name = name
        self.item_effect = item_effect
        self.data_gain = data_gain
        self.can_disable = can_disable
        self.can_scan = can_scan

    # fetches the item's name
    def get_item_name(self):
        return self.name

    # prints what the item does on the terminal.
    def get_item_effect(self):
        return self.item_effect

    # gets data_gain attribute for when player uses a healing item.
    def get_data_gain(self):
        return self.data_gain

    # fetches name
    def get_name(self):
        return self.name

    # checks if the item can give you data (item gives_data attribute must be greater than 0)
    def can_give_you_data(self):
        if self.data_gain > 0:
            return True
        return False

    # checks if the item can scan a location on the map
    def is_a_scan_item(self):
        return self.can_scan
