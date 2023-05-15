# Code by Victor J Wilson
from src.location import Location
# the first thing to be built, you can't have a game without a world to put it in
class World:
    """ Class "World"
        ToDo: Create your name of the world
        ToDo: Create the locations in the world.
        ToDo: Work out anything else that the world would need.

    """
    def __init__(self, name: string):
        self.name = name
        self._locations = []

    def create_location(self, location_name: string):
        location_ = Location(location_name)
        return location_


    def add_location(self, location_: Location):
        self._locations.append(location_)

    # the player can check which part of the world they are in
    def check_location(self, index):
        return self._locations[index]

    # the player uses this to change worlds

    def change_location(self, index, player: Player):
        # change the player's current location index.
        pass



