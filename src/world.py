# Code by Victor J Wilson

from location import Location
from npc import NPC
from item import Item
import random
import json


# the first thing to be built, you can't have a game without a world to put it in
class World:
    """ Class "World"
        ToDo: Create your name of the world
        ToDo: Create the locations in the world.
        ToDo: Work out anything else that the world would need.

    # size of world should be 5 by 5 for a good challenging experience
    """
    def __init__(self):
        self.width = 5
        self.height = 5
        self.map = [['_' for j in range(self.width)] for i in range(self.height)]
        self.position = [-1, -1]  # default position when player is not on the map
        self.npc_list = []
        self.locations = []
        self.items = []

    # writes the map to the text file
    def write_map_to_text_file(self):
        with open("../game_data/world.txt", 'w', encoding="utf-8") as file:
            for i in range(self.height):
                for j in range(self.width):
                    file.write(self.map[i][j])
                file.write("\n")

    # places player in a random position on the using random access
    def place_player(self):
        random_position = random.randint(0, 24)
        with open("../game_data/world.txt", 'r+', encoding="utf-8") as file:
            file.seek(random_position)
            print(random_position)
            file.write('@')

    # marks location as visited
    def mark_as_visited(self):
        self.map[self.position[0]][self.position[1]] = '|'

    # finds where the player is on the map
    def get_player_location(self):
        x = 0
        y = 0
        with open("../game_data/world.txt", 'r', encoding="utf-8") as file:
            for line in file.readlines():
                for char in line:
                    y += 1
                    if char == '@':
                        self.position[0] = x
                        self.position[1] = y
                        break
                x += 1

        print(x, y)
        return self.position

    # the player uses this to change worlds
    def move_to_new_location(self, player_position: list):
        # change the player's current location index.
        x_coordinate = player_position[0]
        y_coordinate = player_position[1]

        if player_position == [-1, -1]:
            print("there is not a player on the map")
        else:
            self.mark_as_visited()
            direction = input()
            match direction:
                case "w":
                    print("you travelled north")
                    if x_coordinate == 0:
                        print("can't move north")
                    else:
                        x_coordinate = x_coordinate-1
                        self.map[x_coordinate][y_coordinate] = '@'
                case "d":
                    if y_coordinate == len(self.map[0]):
                        print("can't move east")
                    else:
                        y_coordinate = y_coordinate + 1
                        self.map[x_coordinate][y_coordinate] = '@'

                case "s":
                    if x_coordinate == len(self.map):
                        print("can't move south")
                    else:
                        x_coordinate = x_coordinate + 1
                        self.map[x_coordinate][y_coordinate] = '@'
                case "a":
                    if y_coordinate == 0:
                        print("can't move west")
                    else:
                        y_coordinate = y_coordinate - 1
                        self.map[x_coordinate][y_coordinate] = '@'

        self.write_map_to_text_file()

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
    new_map = World()
    new_map.write_map_to_text_file()
    new_map.place_player()



