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
        self.data = 50  # data represents HP for this character.
        self.items = []
        self._backpack = BackPack(self.items)
        self.position = []

    # fetches the name given to the player
    def get_player_name(self):
        return self.name

    # fetches the number of items in backpack to display to the terminal, used when displaying backpack contents.
    def get_backpack_count(self):
        return len(self._backpack)

    # gets the player's current position, required when moving the player
    def get_current_position(self):
        return self.position

    # saves the player's current position to be used as reference for when player moves again.
    def save_current_player_position(self, position: list):
        self.position = position

    # get the player's data
    def get_data_remaining(self):
        return self.data

    # this method is called when the player enters a trap room.
    def entered_trap_room(self, location: Location, data: int):
        if not location.is_trap_room():
            return data

        if self._backpack.in_backpack("Anti Virus Module") != -1:
            print("You used the Anti Virus Module protect you from the trap")
            del self._backpack[self._backpack.in_backpack("Anti Virus Module")]
            return data

        data = data - 10
        return data

    # searches location and displays any items in the location that are lying around.
    def search_location(self, location: Location):
        print("You searched the location for an item")
        location_item_list = location.get_items_list()
        if not location_item_list:
            print("No items found in this location")
            return

        for item in location_item_list:
            print("Found {}".format(item.name))

    # adds an item to the backpack.
    def add_item_to_backpack(self, item: Item):
        self._backpack.add(item)

    # prints contents of backpack to terminal, performs the "inventory check" feature of the game.
    def show_inventory(self):
        self._backpack.print_backpack_items()

    def talk_to_npcs(self, npcs: list):
        if not npcs:
            print("Nobody to talk to... Man I feel lonely :(")
        for npc in npcs:
            npc.read_dialogue()
            self._backpack.add(npc.give_item())

    # player reads item effect to the terminal
    def read_item_effect(self, item_name: str):
        item_index = self._backpack.in_backpack(item_name)
        if item_index == -1:
            print("You can't read what you don't have")
        current_item = self._backpack[item_index]
        print(current_item.get_item_effect())

    def has_ip_address(self):
        return self._backpack.in_backpack("IP Address")

    # heals the player when using this item.
    def use_data_gain_item(self, item_name: str, data: int):
        item_index = self._backpack.in_backpack(item_name)
        if item_index == -1:
            print("Using an item you don't have ?! Haven't you hacked enough things already?!")
            return

        current_item = self._backpack[item_index]
        if not current_item.can_give_you_data():
            print("This item won't give you data hahaha!")

        # if the item is data_gain item you gain data
        print("you gained 20 bytes of data")
        data = data + current_item.get_data_gain()
        del self._backpack[item_index]

        return data

    # provides map positions to game for when scanning items in the game.
    def scan_locations(self, item_name: str):
        y_coordinate = self.position[0]
        x_coordinate = self.position[1]
        position_to_be_scanned = []
        """check if item is a scan type item"""
        item_index = self._backpack.in_backpack(item_name)

        if item_index == -1:
            print("Using an item you don't have ?! Haven't you hacked enough things already?!")
            return

        if not self._backpack[item_index].is_a_scan_item:
            print("Good luck trying to do that with this piece of equipment hahaha!")
            return
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
