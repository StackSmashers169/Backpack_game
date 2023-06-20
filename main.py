from __future__ import annotations
from src import Game
from src import Player
from src import World
from src import Location
from src import NPC
from src import Item
from src.player import Player



def game_menu():
    print("To start game type y into the terminal, to quit, type 'q' ")
    command = input()
    while command != "y" and command != "q":
        print("invalid input received! Try again!")
        command = input()

    while command == "y":
        print("==============================================")
        print("Adventure in WEBWorld!")
        for i in range(10):
            print("")
        print("==============================================")
        print("Welcome to WEBWorld!")
        for i in range(10):
            print("")
        print("==============================================")
        print("Enter player name")
        player_name = input()
        new_player = Player(player_name)
        new_world = World()
        new_game = Game(new_world, new_player)
        play_game(new_player)

        print("would you like to play again? type 'y' to play again or 'q' to exit")
        while command != "y" and command != "q":
            print("invalid input received! Try again!")
            command = input()

    print("Exiting Game")
    return


def play_game(new_player: Player):
    player_data = new_player.get_data()
    moves = 0
    location_name = ""
    while location_name != "A Remote Server":

        if player_data == 0:
            print("GAME OVER! You lost connection to Web World :( better luck next time!")
            return new_player

    print("Congratulations! you managed to escape to safety!")
    return new_player
