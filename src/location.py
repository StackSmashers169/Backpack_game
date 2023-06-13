# Code written by Victor J Wilson

class Location:

    def __init__(self, name: str, description: str, visited: bool, has_trap: bool, np_characters: list,
                 items: list, positions: list):
        self.name = name
        self.description = description
        self.visited = visited
        self.has_trap = has_trap

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

