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
        self.test_location = Location("Test Location", "Testing Location", False, False, 1, [], [], [])
        self.test_item = Item("Test Item", "Item that tests the game", 0, False, False)
        self.test_npc = NPC("Test NPC", "Here to help test the server", False, False, [])

    def test_player_movement(self):
        self.test_world.write_map_to_text_file(WORLD_FILEPATH)
        self.test_world.place_player(WORLD_FILEPATH, 2, 2)
        self.assertEqual.
        self.test_world.save_player_position(self.test_player)
        self.test_world.move_to_new_location(WORLD_FILEPATH, self.test_player.get_current_position(), "w")
        self.test_world.save_player_position(self.test_player)
        self.assertEqual(self.test_player.get_current_position(), [1, 2])

    # This is more of a acceptance test than a unit test.
    def test_pick_up_item(self):
        self.test_world.write_map_to_text_file(WORLD_FILEPATH)
        self.test_game.load_game_assets(LOCATIONS_FILEPATH, ITEMS_FILEPATH, NPC_FILEPATH)
        self.test_game.build_world(WORLD_FILEPATH)
        self.test_world.save_player_position(self.test_player)
        self.test_world.move_to_new_location(WORLD_FILEPATH, self.test_player.get_current_position(), "w")
        self.test_world.save_player_position(self.test_player)

        """get location name"""
        current_location = self.test_game.enter_location(self.test_player.get_current_position())
        location_name = current_location.get_location_name()

        """add item via talking to npc or adding to back pack immediately"""
        if location_name == "Database Room" or location_name == "Connection Hub" or location_name == "Internet Forum" \
                or location_name == "API Store" or location_name == "BCOM Bitcoin Mine":
            """talk to npcs if the item is obtained from them"""
            location_npcs = current_location.get_npc_list()
            self.test_player.talk_to_npcs(location_npcs)

            """get the location's specific item and add it if its a location with an assigned item"""
            location_item = current_location.get_specific_item()
            self.test_player.add_item_to_backpack(location_item)
            self.assertEqual(self.test_player.get_backpack_count(), 1)
        else:
            location_npcs = current_location.get_npc_list()
            self.test_player.talk_to_npcs(location_npcs)

            """get the location's specific item and add it if its a location with an assigned item"""
            location_item = current_location.get_specific_item()
            self.test_player.add_item_to_backpack(location_item)
            self.assertEqual(self.test_player.get_backpack_count(), 0)
