from game import Game
from world import World
from player import Player
from backpack import BackPack
from location import Location
from item import Item
from npc import NPC


print("A Hacker's adventure in Web World!")
for i in range(10):
    print("")
print("Welcome to Web World!")
for i in range(10):
    print("")

print("Enter player name")
player_name = input()
new_player = Player(player_name)
new_world = World()
new_game = Game(new_world, new_player)
