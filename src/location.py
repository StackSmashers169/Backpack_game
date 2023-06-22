# Code written by Victor J Wilson
from src.item import Item
from src.npc import NPC


class Location:

    def __init__(self, name: str, description: str, visited: bool, has_trap: bool, max_positions: int,
                 np_characters: list, items: list, positions: list):
        self.name = name
        self.description = description
        self.visited = visited
        self.has_trap = has_trap
        self.max_positions = max_positions
        self._npc_list = []
        self._items_list = []
        self._world_positions = []

        if np_characters is None:
            np_characters = []
        for npcs in np_characters:
            self._npc_list.append(npcs)

        if items is None:
            items = []
        for item in items:
            self._items_list.append(item)

        if positions is None:
            positions = []
        for position in positions:
            self._world_positions.append(position)

    def read_location_description(self):
        print(self.description)

    # this method is called when building the world
    def assign_map_position(self, position: list):
        self._world_positions.append(position)

    # called when building world
    def assign_item(self, item: Item):
        self._items_list.append(item)

    # this method is called when building the world
    def assign_npc(self, npc: NPC):
        self._npc_list.append(npc)

    # gets location name in order to fulfill game objective requirements
    def get_location_name(self):
        return self.name

    # method for testing purposes, might delete later if it doesn't come up during game loop
    def get_positions(self):
        return self._world_positions

    def set_location_to_visited(self):
        if not self.visited:
            self.visited = True
    # called when entering a new location, change that location from visited = false to visited = true

    def is_visited(self):
        return self.visited

    # checks if the room is a trap room
    def is_trap_room(self):
        return self.has_trap

    # gets a list of items for the player to view when they search the location
    def get_items_list(self):
        return self._items_list

    # called when player gets item from location
    def get_specific_item(self):
        if not self._items_list:
            print("no items in this location")
            return
        return self._items_list.pop(0)

    # gets a list of npcs to talk to.
    def get_npc_list(self):
        return self._npc_list

    # matches position on board with location assigned to it, essential for knowing which location the player is at
    # or when player is scanning an adjacent or adjacent tiles.
    def match_position(self, map_position: list):
        for position in self._world_positions:
            if map_position == position:
                return True
        return False







