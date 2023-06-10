# Code by Victor J Wilson
# from src.location import Location
from src.player import Player
import os


# the first thing to be built, you can't have a game without a world to put it in
class World:
    """ Class "World"
        ToDo: Create your name of the world
        ToDo: Create the locations in the world.
        ToDo: Work out anything else that the world would need.

    """
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.map = [['◇' for j in range(width)] for i in range(height)]
        self.position = [-1, -1]  # default position when player is not on the map

    # places player icon onto the map
    def place_player(self, y_coordinate, x_coordinate):
        self.map[y_coordinate][x_coordinate] = '🞯'
        self.print_map()
        print("player entered world successfully \n")

    # marks location as visited
    def mark_as_visited(self):
        self.map[self.position[0]][self.position[1]] = '◈'

    def interact(self, location_name: str):
        # find the index player is at currently
        pass

    # finds where the player is
    def check_location(self):

        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == '🞯':
                    self.position = [i, j]
        return self.position

    # the player uses this to change worlds
    def move_to_new_location(self, player_position):
        # change the player's current location index.
        x_coordinate = player_position[0]
        y_coordinate = player_position[1]
        print("enter a direction: ")
        if player_position == [-1, -1]:
            print("there is not a player on the map")
        else:
            self.mark_as_visited()
            direction = input()
            match direction:
                case "n":
                    print("you travelled north")
                    if x_coordinate == 0:
                        print("can't move north")
                    else:
                        x_coordinate = x_coordinate-1
                        self.map[x_coordinate][y_coordinate] = '🞯'
                case "e":
                    if y_coordinate == len(self.map[0]):
                        print("can't move east")
                    else:
                        y_coordinate = y_coordinate + 1
                        self.map[x_coordinate][y_coordinate] = '🞯'

                case "s":
                    if x_coordinate == len(self.map):
                        print("can't move south")
                    else:
                        x_coordinate = x_coordinate + 1
                        self.map[x_coordinate][y_coordinate] = '🞯'
                case "w":
                    if y_coordinate == 0:
                        print("can't move west")
                    else:
                        y_coordinate = y_coordinate - 1
                        self.map[x_coordinate][y_coordinate] = '🞯'

        self.write_map_to_text_file()

    def write_map_to_text_file(self):
        file = open("game_data/map.txt")
        if os.path.getsize("/game_data/map.txt") == 0:
            for i in range(self.height):
                for j in range(self.width):
                    file.write(self.map[i][j])
                file.write("\n")

    def load_locations(self):
        pass

    def load_items(self):
        pass

    def load_npcs(self):
        pass

if __name__ == "__main__":
    new_map = World(5, 5)
    new_map.place_player(1, 2)
    new_map.move_to_new_location(new_map.check_location())


