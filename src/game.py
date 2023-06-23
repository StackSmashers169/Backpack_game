# code by Victor J Wilson
from src.player import Player
from src.world import World
from src.location import Location
from src.npc import NPC
from src.item import Item
import json
import random
import os


# this class handles all game operations and logic, includes a main function for playing the game.
class Game:

    def __init__(self, world: World, player: Player):
        self.world = world
        self.npc_list = []
        self.locations = []
        self.items = []
        self.player = player

    # =================================Loading Game Assets====================================
    # loads location data
    def load_locations(self, locations_path="../game_data/locations.json"):
        try:
            with open(locations_path, 'r', encoding='utf-8') as file_handle:
                locations_data = json.load(file_handle)
                for location in locations_data.values():
                    name = location["name"]
                    description = location["description"]
                    visited = location["visited_status"]
                    has_trap = location["has_trap"]
                    max_positions = location["max_positions"]
                    npcs = location["np_characters"]
                    items = location["items"]
                    locations = location["positions"]
                    location = Location(name, description, visited, has_trap, max_positions,
                                        npcs, items, locations)
                    self.locations.append(location)
        except FileNotFoundError:
            print(f'File {locations_path} not found')
        except IOError:
            print(f'Unable to read file: {locations_path} ')
        except json.JSONDecodeError as json_err:
            print(json_err)

    def load_items(self, items_path="../game_data/items.json"):
        try:
            with open(items_path, 'r', encoding='utf-8') as file_handle:
                items_data = json.load(file_handle)
                for item in items_data.values():
                    name = item["name"]
                    effect = item["item_effect"]
                    data_gain = item["data_gain"]
                    can_disable = item["can_disable"]
                    can_scan = item["can_scan"]
                    this_item = Item(name, effect, data_gain, can_disable, can_scan)
                    self.items.append(this_item)
        except FileNotFoundError:
            print(f'File {items_path} not found')
        except IOError:
            print(f'Unable to read file {items_path}')
        except json.JSONDecodeError as json_err:
            print(json_err)

    # function that loads npc information into npc class
    def load_npc(self, npc_path="../game_data/np_characters.json"):
        try:
            with open(npc_path, 'r', encoding='utf-8') as file_handle:
                npc_data = json.load(file_handle)
                for np_character in npc_data.values():
                    name = np_character["name"]
                    dialogue = np_character["dialogue"]
                    gives_item = np_character["gives_item"]
                    damages_you = np_character["damages_you"]
                    items = np_character["items"]
                    npc = NPC(name, dialogue, gives_item, damages_you, items)
                    self.npc_list.append(npc)
        except FileNotFoundError:
            print(f'File {npc_path} not found')
        except IOError:
            print(f'Unable to read file: {npc_path}')
        except json.JSONDecodeError as json_err:
            print(json_err)

    # =================================Building Game World====================================
    # each spot on the grid must be assigned a location.
    # 4 for each of the types of empty room (8 total)
    # 5 for each trap room (10 total)
    # One for each of the unique locations (7) total
    def assign_locations(self, map_positions: list):
        # create a dictionary of key location object and value count
        # of the 11 different locations.
        random.shuffle(map_positions)
        fill_positions = 0
        count = 0
        for location in self.locations:
            while fill_positions < location.max_positions and count < len(map_positions):
                location.assign_map_position(map_positions[count])
                count += 1
                fill_positions += 1
            fill_positions = 0

    # unique locations have a specific item so assign them accordingly.
    # to speed up process cases with only one item addition have break statements.
    def assign_items_to_locations(self):

        for location in self.locations:
            unique_location = location.name
            # match case items
            match unique_location:
                case "Database Room":
                    for index in range(len(self.items)):
                        if self.items[index].get_name() == "IP Address":
                            location.assign_item(self.items[index])
                            break

                case "Connection Hub":
                    for index in range(len(self.items)):
                        if self.items[index].get_name() == "Bit Bucket":
                            location.assign_item(self.items[index])
                            break

    # to speed up process cases with only one npc addition have break statements.
    def assign_npcs_to_locations(self):
        for location in self.locations:
            unique_location = location.name

            match unique_location:
                case "Database Room":
                    for index in range(len(self.npc_list)):
                        if self.npc_list[index].get_name() == "Database Maintenance Crew":
                            location.assign_npc(self.npc_list[index])
                            break

                case "Connection Hub":
                    for index in range(len(self.npc_list)):
                        if self.npc_list[index].get_name() == "Middle Man" or \
                                self.npc_list[index].get_name() == "Random Script Kiddie":
                            location.assign_npc(self.npc_list[index])

                case "Internet Forum":
                    for index in range(len(self.npc_list)):
                        if self.npc_list[index].get_name() == "Angry Forum Crowd" or \
                                self.npc_list[index].get_name() == "Frustrated Hacker":
                            location.assign_npc(self.npc_list[index])

                case "Honeypot Server":
                    for index in range(len(self.npc_list)):
                        if self.npc_list[index].get_name() == "Server Security":
                            location.assign_npc(self.npc_list[index])
                            break

                case "API Store":
                    for index in range(len(self.npc_list)):
                        if self.npc_list[index].get_name() == "API Salesperson":
                            location.assign_npc(self.npc_list[index])
                            break

                case "BCOM Bitcoin Mine":
                    for index in range(len(self.npc_list)):
                        if self.npc_list[index].get_name() == "Bitcoin Miner Adam":
                            location.assign_npc(self.npc_list[index])
                            break

    def assign_item_to_npc(self):
        for npc in self.npc_list:
            npc_with_item = npc.name

            match npc_with_item:
                case "Random Script Kiddie":
                    for index in range(len(self.items)):
                        if self.items[index].get_name() == "Packet Scanner":
                            npc.assign_item(self.items[index])

                case "Frustrated Hacker":
                    for index in range(len(self.items)):
                        if self.items[index].get_name() == "Anti Virus Module":
                            npc.assign_item(self.items[index])

                case "API Salesperson":
                    for index in range(len(self.items)):
                        if self.items[index].get_name() == "Wireshark":
                            npc.assign_item(self.items[index])

                case "Bitcoin Miner Adam":
                    for index in range(len(self.items)):
                        if self.items[index].get_name() == "Byte Package":
                            npc.assign_item(self.items[index])

    # =================================Game Mechanics====================================

    # matches current player position with location, otherwise
    # return default (this should never happen since every position has a location assigned)
    def enter_location(self, position: list):
        for index in range(len(self.locations)):
            if self.locations[index].match_position(position):
                print("Entered {}".format(self.locations[index].get_location_name()))
                self.locations[index].read_location_description()
                self.locations[index].set_location_to_visited()
                return self.locations[index]
        return self.locations[0]

    # if player has item "self.backpack"
    def goal_marker_activate(self, path: str, player: Player):
        if player.has_ip_address() == -1:
            return

        print("Obtained the IP Address, now you can see where you need to go!")
        position = []
        for location in self.locations:
            if location.name == "A Remote Server":
                position = location.get_positions()  # the remote server room has only one location
        with open(path, 'r+', encoding="utf-8") as file:
            width = len(file.readline()) + 1  # for some reason width won't catch the \r character
            # for posix systems width needs to be +1 the grid width instead of +2 for windows.
            if os.name == 'posix':
                width = len(file.readline())

            winning_position = position[0][0] * width + position[0][1]
            file.seek(winning_position)
            file.write('X')

        self.world.read_map_to_terminal(path)

    # prints the name of the location at the position given in parameters and marks it with 'M' on the map
    def print_scanned_locations(self, position: list, path: str):
        for index in range(len(self.locations)):
            if self.locations[index].match_position(position):
                print("Scanned Location: {} "
                      " location is marked with M".format(self.locations[index].get_location_name()))

        with open(path, 'r+', encoding="utf-8") as file:
            width = len(file.readline()) + 1  # for some reason width won't catch the \r character
            # for posix systems width needs to be +1 the grid width instead of +2 for windows.
            if os.name == 'posix':
                width = len(file.readline())

            winning_position = position[0][0] * width + position[0][1]
            file.seek(winning_position)
            file.write('M')

        self.world.read_map_to_terminal(path)

    # =================================Running and Playing the Game====================================
    def location_interaction_message(self):
        print("What would you like to do? Type 'l' to search location, 'c' to add item, 't' to talk to npc"
              " 'i' to check backpack contents, \n r to read item effect, h to use a heal item, f to use a scan item"
              " 'm' to move to a new location")

        # Builds the game world, assigning locations to positions, items and characters to locations and items to
        # characters, also resets map from previous game iteration.

    # if you have the item "IP Address"
    def load_game_assets(self, locations_path: str, items_path: str, npc_path: str):
        self.load_locations(locations_path)
        self.load_items(items_path)
        self.load_npc(npc_path)

    # calls all the methods that build the game world (assigning locations to positions, items and NPCs to locations)
    def build_world(self, world_path: str):
        self.assign_locations(self.world.get_positions_as_list())
        self.assign_items_to_locations()
        self.assign_npcs_to_locations()
        self.assign_item_to_npc()

        """place the player in the first position in Empty Room A, in the future I plan to make a separate room
        called "start_room" """
        self.world.write_map_to_text_file(world_path)
        player_position = self.locations[0].get_positions()
        self.world.place_player(world_path, player_position[0][0], player_position[0][1])

    # when the game ends need to empty all lists in game, so we can reload the game
    # without appending to the list from the previous game iteration.
    def delete_lists(self):
        self.locations.clear()
        self.npc_list.clear()
        self.items.clear()


# main function for testing purposes
if __name__ == "__main__":
    test_world = World()
    test_player = Player("test")
    test_game = Game(test_world, test_player)
    """Test your methods below"""
