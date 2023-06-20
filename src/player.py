# code by Victor J Wilson(20094873)


from backpack import BackPack
from item import Item
from location import Location
from npc import NPC

class Player:

    def __init__(self, name: str):
        self.name = name
        self.is_alive = True
        self.data = 50  # data represents HP for this character or more precisely 50b.
        self.items = []
        self.backpack = BackPack(self.items)
        self.position = []

    # searches location for an item
    def search_location(self, location: Location):
        print("You searched the location for an item")

    # if an NPC(s) exists in this location you can talk to them.
    def talk_to_npc(self):
        pass

    # searches for the item and then uses it, then "pops" the item from the backpack.
    def use_item(self, item):
        pass

    # if player enters trap room this will happen.
    def entered_trap_room(self, location: Location):
        pass

