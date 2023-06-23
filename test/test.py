from src.player import Player
from src.game import Game
from src.location import Location
from src.world import World
from src.item import Item
from src.npc import NPC


import unittest

WORLD_FILEPATH = "../game_data/world.txt"
LOCATIONS_FILEPATH = "../game_data/locations.json"
ITEMS_FILEPATH = "../game_data/items.json"
NPC_FILEPATH = "../game_data/np_characters.json"


class TestStack(unittest.TestCase):
    def setUp(self):
        self.test_player = Player("Test")
        self.test_world = World()
        self.test_game = Game(self.test_world, self.test_player)

    def test_player_movement(self):
        self.test_world.write_map_to_text_file(WORLD_FILEPATH)
        self.test_world.place_player(WORLD_FILEPATH, 2, 2)
        self.test_world.save_player_position(self.test_player)
        self.test_world.move_to_new_location(WORLD_FILEPATH, self.test_world.position, "w")
        self.test_world.save_player_position(self.test_player)
        self.assertEqual(self.test_player.get_current_position(), [1, 2])

    def test_pick_up_item(self):
        self.test_world.write_map_to_text_file(WORLD_FILEPATH)

