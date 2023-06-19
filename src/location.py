# Code written by Victor J Wilson
from item import Item
from npc import NPC


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
            self._world_positions = []

    def read_location_description(self):
        print(self.description)

    def add_map_position(self, position: list):
        self._world_positions.append(position)

    def add_item(self, item: Item):
        self._items_list.append(item)

    def add_npc(self, npc: NPC):
        self._npc_list.append(npc)

    # different locations will do different things to the player
    def get_location_name(self):
        return self.name

    def trap_room(self, data: int):
        data = data - 10
        return data

    """Entering the Honeypot server forces you to interact with server security which drops your data to 0"""
    def server_security(self, data: int):
        data = 0
        return data

    def get_positions(self):
        return self._world_positions

    def get_items(self):
        return self._items_list

    def get_npcs(self):
        return self._npc_list
