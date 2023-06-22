# code by Victor J Wilson(20094873)

from src.backpack import BackPack
from src.location import Location
from src.npc import NPC
from src.item import Item

WORLD_FILEPATH = "../game_data/world.txt"


class Player:

    def __init__(self, name: str):
        self.name = name
        self.is_alive = True
        self.data = 50  # data represents HP for this character or more precisely 50b.
        self.items = []
        self._backpack = BackPack(self.items)
        self.position = []

    # gets the player's current position, required when moving the player
    def get_current_position(self):
        return self.position

    # get the player's data
    def get_data_remaining(self):
        return self.data

    def entered_trap_room(self, location: Location, data: int):
        if not location.is_trap_room():
            return data

        if self._backpack.in_backpack("Anti Virus Module") != -1:
            del self._backpack[self._backpack.in_backpack("Anti Virus Module")]
            return data

        data = data - 10
        return data

    # searches location for an item
    def search_location(self, location: Location):
        print("You searched the location for an item")
        location_item_list = location.get_items_list()
        if not location_item_list:
            print("No items found in this location")
            return

        for item in location_item_list:
            print("Found {}".format(item.name))

    def add_item_to_backpack(self, item: Item):
        self._backpack.add(item)

    def show_inventory(self):
        self._backpack.print_backpack_items()

    def talk_to_npcs(self, npcs: list):
        for npc in npcs:
            npc.read_dialogue()
            self._backpack.add(npc.gives_item())

    def read_item_effect(self, item_name: str):
        item_index = self._backpack.in_backpack(item_name)
        if item_index == -1:
            print("You can't read what you don't have")
        current_item = self._backpack[item_index]
        print(current_item.get_item_effect)

    def has_ip_address(self):
        return self._backpack.in_backpack("IP Address")

    def use_item(self, item_name: str):
        item_index = self._backpack.in_backpack(item_name)
        if item_index == -1:
            print("Using an item you don't have ?! Haven't you hacked enough things already?!")
            return

        current_item = self._backpack[item_index]
        if not current_item.can_be_used():
            print("You can't use this item")

        if current_item.is_a_scan_item():
            self.scan_locations(item_name)
            del self._backpack[item_index]

        # if the item is data_gain item you gain data
        self.data = current_item.get_data_gain()
        del self._backpack[item_index]

    # provides map positions to game for when scanning items in the game.
    def scan_locations(self, item_name: str):
        y_coordinate = self.position[0]
        x_coordinate = self.position[1]
        position_to_be_scanned = []
        # ==============================Packet Scanner===================================
        if item_name == "Packet Scanner":
            command = input()
            while command != 'w' and command != 'a' and command != 's' and command != 'd':
                print("invalid input received, please enter w, a, s or d: ")
                command = input()

            match command:
                case "w":
                    if y_coordinate == 0:
                        return position_to_be_scanned
                    else:
                        y_coordinate = y_coordinate - 1
                        position_to_be_scanned = [y_coordinate, x_coordinate]
                        return position_to_be_scanned

                case "d":
                    if x_coordinate == 4:
                        return position_to_be_scanned
                    else:
                        x_coordinate = x_coordinate + 1
                        position_to_be_scanned = [y_coordinate, x_coordinate]
                        return position_to_be_scanned

                case "s":
                    if y_coordinate == 4:
                        return position_to_be_scanned
                    else:
                        y_coordinate = y_coordinate + 1
                        position_to_be_scanned = [y_coordinate, x_coordinate]
                        return position_to_be_scanned

                case "a":
                    if x_coordinate == 0:
                        return position_to_be_scanned
                    else:
                        x_coordinate = x_coordinate - 1
                        position_to_be_scanned = [y_coordinate, x_coordinate]
                        return position_to_be_scanned

        # ==============================Wireshark===================================
        print("enter y_coordinate")
        y_coordinate = int(input())

        while 0 > y_coordinate > 4:
            print("entered a coordinate outside the world bounds")
            y_coordinate = int(input())

        print("enter x_coordinate")
        x_coordinate = int(input())

        while 0 > x_coordinate > 4:
            print("entered a coordinate outside the world bounds")
            x_coordinate = int(input())

        position_to_be_scanned = [y_coordinate, x_coordinate]
        return position_to_be_scanned
