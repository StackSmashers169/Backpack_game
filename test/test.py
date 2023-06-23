from src.player import Player
from src.game import Game
from src.location import Location
from src.world import World
from src.item import Item
from src.npc import NPC

import unittest


class TestStack(unittest.TestCase):
    def setup(self):
        test_player = Player("Test")
        test_world = World()
        test_game = Game(test_world, test_player)

