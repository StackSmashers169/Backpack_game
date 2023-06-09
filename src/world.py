# Code by Victor J Wilson
import os
from src.player import Player


# the first thing to be built, you can't have a game without a world to put it in
class World:
    """ Class "World"
        ToDo: Create your name of the world
        ToDo: Create the locations in the world.
        ToDo: Work out anything else that the world would need.

    # size of world should be 5 by 5 for a good challenging experience
    """

    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height
        self.map = [['_' for j in range(self.width)] for i in range(self.height)]
        self.position = [-1, -1]  # default position when player is not on the map
        self.name = "Web World"

    # writes the map to the text file and then prints same map to terminal
    def write_map_to_text_file(self, path: str):
        with open(path, 'w') as file:
            for i in range(self.height):
                for j in range(self.width):
                    file.write(self.map[i][j])
                file.write("\n")

    # writes the map into the terminal so player can keep track of it.
    def read_map_to_terminal(self, path: str):
        with open(path, 'r') as file:
            game_map = file.read()
            print(game_map)

    # places player in a random position on the using random access
    def place_player(self, path: str, pos_y: int, pos_x: int):
        print("You managed to escape to this empty room!, hurry up and get the data to the remote server! before the"
              "admin catches you!")
        y_coordinate = pos_y
        x_coordinate = pos_x
        with open(path, 'r+', encoding="utf-8") as file:
            width = len(file.readline()) + 1  # for some reason width won't catch the \r character
            # for posix systems width needs to be +1 the grid width instead of +2 for windows.
            if os.name == 'posix':
                width = len(file.readline())

            position = y_coordinate * width + x_coordinate
            file.seek(position)
            file.write('@')
        self.position[0] = y_coordinate
        self.position[1] = x_coordinate
        self.read_map_to_terminal(path)

    def update_player_location(self, path: str, player_position: list):
        y_coordinate = player_position[0]
        x_coordinate = player_position[1]
        with open(path, 'r+', encoding="utf-8") as file:
            width = len(file.readline()) + 1  # for some reason width won't catch the \r character
            # for posix systems width needs to be +1 the grid width instead of +2 for windows.
            if os.name == 'posix':
                width = len(file.readline())

            position = y_coordinate * width + x_coordinate
            file.seek(position)
            file.write('@')
        self.position[0] = y_coordinate
        self.position[1] = x_coordinate
        self.read_map_to_terminal(path)

    # function for moving player around the world
    def move_to_new_location(self, path: str, player_position: list, direction_input: str):
        # change the player's current location index.
        y_coordinate = player_position[0]
        x_coordinate = player_position[1]

        with open(path, 'r+', encoding="utf-8") as file:
            width = len(file.readline()) + 1  # for some reason width won't catch the \r character
            # for posix systems width needs to be +1 the grid width instead of +2 for windows.
            if os.name == 'posix':
                width = len(file.readline())

            position = y_coordinate * width + x_coordinate
            file.seek(position)
            file.write('|')

        if player_position == [-1, -1]:
            print("there is not a player on the map")
        else:
            direction = direction_input

            match direction:
                case "w":
                    if y_coordinate == 0:
                        print("can't move north")
                    else:
                        print("you travelled north")
                        y_coordinate = y_coordinate - 1
                        self.map[y_coordinate][x_coordinate] = '@'

                case "d":
                    if x_coordinate == self.width - 1:
                        print("can't move east")
                    else:
                        print("you travelled east")
                        x_coordinate = x_coordinate + 1
                        self.map[y_coordinate][x_coordinate] = '@'

                case "s":
                    if y_coordinate == self.height - 1:
                        print("can't move south")
                    else:
                        print("you travelled south")
                        y_coordinate = y_coordinate + 1
                        self.map[y_coordinate][x_coordinate] = '@'

                case "a":
                    if x_coordinate == 0:
                        print("can't move west")
                    else:
                        print("you travelled west")
                        x_coordinate = x_coordinate - 1
                        self.map[y_coordinate][x_coordinate] = '@'

        player_position[0] = y_coordinate
        player_position[1] = x_coordinate
        self.update_player_location(path, player_position)

    def get_positions_as_list(self):
        position_list = []
        for i in range(self.height):
            for j in range(self.width):
                position_list.append([i, j])

        return position_list

    def save_player_position(self, player: Player):
        player.save_current_player_position(self.position)

    # if the player obtained the item "IP Address" the game marks the location with "X"


if __name__ == "__main__":
    new_map = World()
    # test any "world" methods below
