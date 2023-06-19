# code by Victor J Wilson
from player import Player
from world import World
from location import Location
from npc import NPC
from item import Item
import json
import random


# this class handles all game operations and logic, includes a main function for playing the game.
class Game:

    def __init__self(self, world: World, player: Player):
        self.world = world
        self.player = player
        self.npc_list = []
        self.locations = []
        self.items = []

    # loads location data
    def load_locations(self, locations_info="../game_data/locations.json"):
        try:
            with open(locations_info, 'r', encoding='utf-8') as file_handle:
                locations_data = json.load(file_handle)
                for location in locations_data.values():
                    name = location["name"]
                    description = location[description]
                    visited = location["visited_status"]
                    has_trap = location["has_trap"]
                    max_positions = location["max_positions"]
                    npcs = location["np_characters"]
                    items = location["items"]
                    positions = location["positions"]
                    location = Location(name, description, visited, has_trap, max_positions,
                                        npcs, items, positions)
                    self.locations.append(location)
        except FileNotFoundError:
            print(f'File {locations_info} not found')
        except IOError:
            print(f'Unable to read file: {locations_info} ')
        except json.JSONDecodeError as json_err:
            print(json_err)

    def load_items(self, item_info="../game_data/items.json"):
        try:
            with open(item_info, 'r', encoding='utf-8') as file_handle:
                items_data = json.load(file_handle)
                for item in items_data.values():
                    name = item["name"]
                    effect = item["item_effect"]
                    data_gain = item["data_gain"]
                    can_disable = item["can_disable"]
                    this_item = Item(name, effect, data_gain, can_disable)
                    self.items.append(this_item)
        except FileNotFoundError:
            print(f'File {item_info} not found')
        except IOError:
            print(f'Unable to read file {item_info}')
        except json.JSONDecodeError as json_err:
            print(json_err)

    # function that loads npc information into npc class
    def load_npc(self, npc_info="../game_data/np_characters.json"):
        try:
            with open(npc_info, 'r', encoding='utf-8') as file_handle:
                npc_data = json.load(file_handle)
                for np_character in npc_data.values():
                    name = np_character["name"]
                    dialogues = np_character["dialogues"]
                    action = np_character["action"]
                    npc = NPC(name, dialogues, action)
                    self.npc_list.append(npc)
        except FileNotFoundError:
            print(f'File {npc_info} not found')
        except IOError:
            print(f'Unable to read file: {npc_info}')
        except json.JSONDecodeError as json_err:
            print(json_err)

    # each spot on the grid must be assigned a location.
    # 4 for each of the types of empty room (8 total)
    # 5 for each trap room (10 total)
    # One for each of the unique locations (7) total
    def assign_locations(self, positions: list):
        # create a dictionary of key location object and value count
        # of the 11 different locations.
        random.shuffle(positions)
        fill_positions = 0
        count = 0
        for location in self.locations:
            while fill_positions < location.max_positions or count == len(positions):
                location.add_map_position(positions[count])
                count += 1
                fill_positions += 1
            fill_positions = 0

    # unique locations have a specific item so assign them accordingly.
    # to speed up process cases with only one item addition have break statements.
    def assign_items_to_locations(self):

        for location in self.locations:
            item = location.name
            # match case items
            match item:
                case "Database room":
                    for index in range(len(self.items)):
                        if self.items[index].get_name() == "IP Address":
                            location.add_item(self.items[index])
                            break

                case "Connection Hub":
                    for index in range(len(self.items)):
                        if self.items[index].get_name() == "Bit Bucket" or \
                                self.items[index].get_name() == "Packet Scanner":
                            location.add_item(self.items[index])

                case "Internet Forum":
                    for index in range(len(self.items)):
                        if self.items[index].get_name() == "Anti Virus Module":
                            location.add_item(self.items[index])
                            break

                case "API Store":
                    for index in range(len(self.items)):
                        if self.items[index].get_name() == "Wireshark":
                            location.add_item(self.items[index])
                            break

                case "BCOM Bitcoin Mine":
                    for index in range(len(self.items)):
                        if self.items[index].get_name() == "byte_package":
                            location.add_item(self.items[index])
                            break

    # to speed up process cases with only one npc addition have break statements.
    def assign_npcs_to_locations(self):
        for location in self.locations:
            item = location.name

            match item:
                case "Database_Room":
                    for index in range(len(self.npc_list)):
                        if self.npc_list[index].get_name() == "Database Maintenace Crew":
                            location.add_npc(self.npc_list[index])
                            break

                case "Connection Hub":
                    for index in range(len(self.npc_list)):
                        if self.npc_list[index].get_name() == "Middle Man" or \
                                self.npc_list[index].get_name() == "Random Script Kiddie":
                            location.add_npc(self.npc_list[index])

                case "Internet Forum":
                    for index in range(len(self.npc_list)):
                        if self.npc_list[index].get_name() == "Angry Forum Crowd" or \
                                self.npc_list[index].get_name() == "Frustrated Hacker":
                            location.add_npc(self.npc_list[index])

                case "Honeypot Server":
                    for index in range(len(self.npc_list)):
                        if self.npc_list[index].get_name() == "Server Security":
                            location.add_npc(self.npc_list[index])
                            break

                case "API Store":
                    for index in range(len(self.npc_list)):
                        if self.npc_list[index].get_name() == "API Salesperson":
                            location.add_npc(self.npc_list[index])
                            break

                case "BCOM Bitcoin Mine":
                    for index in range(len(self.npc_list)):
                        if self.npc_list[index].get_name() == "Bitcoin Miner Adam":
                            location.add_npc(self.npc_list[index])
                            break

    # now that we've loaded everything let's start playing the game
    # first introduce the player to the world of the game.
    def game_intro(self):
        print("A Hacker's adventure in Web World!")
        for i in range(10):
            print("")
        print("Welcome to Web World!")


if __name__ == "__main__":
    pass
