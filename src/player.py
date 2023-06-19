# code by Victor J Wilson(20094873)


from backpack import BackPack
from item import Item
from location import Location


class Player:

    def __init__(self, name: str):
        self.name = name
        self.is_alive = True
        self.data = 50  # data represents HP for this character or more precisely 50b.
        self.items = []
        self.backpack = BackPack(self.items)
        self.position = []

    # saves the player's position on the map (might implement this outside of the project
    # since saving the map isn't a requirement)
    def save_position(self, x_coordinate, y_coordinate):
        pass

    # searches location for an item
    def search_location(self):
        pass

    # if an NPC(s) exists in this location you can talk to them.
    def talk_to_npc(self):
        pass

    # called if player triggers a gain_hp tile
    def gain_data(self):
        pass

    # if player enters trap room this will happen.
    def entered_trap_room(self, location: Location):
        if location.get_location_name() == "Data Fragmentation Trap":
            location.read_location_description()
            self.data = self.data - 10

        if location.get_location_name == "Corrupt Data Packet":
            location.read_location_description()
            self.data = self.data - 10

