# code by Victor J Wilson
from player import Player
from world import World
from location import Location
from npc import NPC
from item import Item
import json


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
                    npcs = location["np_characters"]
                    items = location["items"]
                    positions = location["positions"]
                    location = Location(name, description, visited, has_trap, npcs, items, positions)
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


if __name__ == "__main__":
    pass


