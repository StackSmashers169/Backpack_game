from __future__ import annotations
from src.player import Player
from src.game import Game
from src.location import Location
from src.world import World
from src.item import Item
from src.npc import NPC


WORLD_FILEPATH = "game_data/world.txt"
LOCATIONS_FILEPATH = "game_data/locations.json"
ITEMS_FILEPATH = "game_data/items.json"
NPC_FILEPATH = "game_data/np_characters.json"


def play_game(new_player: Player):
    """create instances of all the classes required in the game"""
    world = World()
    new_game = Game(world, new_player)
    new_game.load_game_assets(LOCATIONS_FILEPATH, ITEMS_FILEPATH, NPC_FILEPATH)
    new_game.build_world(WORLD_FILEPATH)
    world.save_player_position(new_player)
    """now we've set up the game world, let's start playing the game"""
    player_data = new_player.get_data_remaining()
    moves = 0
    location_name = ""

    while location_name != "A Remote Server":
        """moving to new location"""
        print("{} has {} data".format(new_player.name, player_data))
        world.move_to_new_location(WORLD_FILEPATH, new_player.position)
        world.save_player_position(new_player)

        """ location data"""
        current_location = new_game.enter_location(new_player.position)
        location_name = current_location.get_location_name()
        if location_name == "A Remote Server":
            return new_player

        """trap room effect"""
        player_data = new_player.entered_trap_room(current_location, player_data)
        if player_data == 0:
            print("Lost connection from WEBWorld :( better luck next time!")
            return new_player

        """interacting with the location and checking inventory"""
        new_game.location_interaction_message()
        command = input()
        while command != 'f' and command != 'c' and command != 't' and command != 'i' and command != 'm'\
                and command != 'u' and command != 'r':
            print("invalid input received, please enter l, c, t, i, r, h, f, or m")
            command = input()

        while command != 'm':
            if command == "l":
                new_player.search_location(current_location)
                new_game.location_interaction_message()


            if command == "c":
                location_item = current_location.get_specific_item()
                new_player.add_item_to_backpack(location_item)
                new_game.location_interaction_message()


            if command == "t":
                location_npcs = current_location.get_npc_list()
                new_player.talk_to_npcs(location_npcs)
                new_game.location_interaction_message()

            if command == "i":
                new_player.show_inventory()
                new_game.location_interaction_message()

            if command == "r":
                print("To read an item, type the name of the item in your backpack")
                item_name = input()
                new_player.read_item_effect(item_name)
                new_game.location_interaction_message()

            if command == "h":
                print("To use an item, type the name of the item in your backpack")
                item_name = input()
                new_player.use_data_gain_item(item_name)
                new_game.location_interaction_message()

            if command == "f":
                print("To use an item, type the name of the item in your backpack")
                item_name = input()
                scanned_position = new_player.scan_locations(item_name)
                new_game.print_scanned_locations(scanned_position)
                new_game.location_interaction_message()

            command = input()
        """showing the location we need to reach if we pick up IP Address"""
        new_game.goal_marker_activate(WORLD_FILEPATH, new_player)



    """be sure to empty all lists and re-write the map file"""
    new_game.delete_lists()
    print("Congratulations! you managed to escape to safety!")
    return new_player


if __name__ == '__main__':
    print("To start game type y into the terminal, to quit, type 'q' ")
    command = input()
    while command != "y" and command != "q":
        print("invalid input received! Try again!")
        command = input()

    while command == "y":
        print("==============================================")
        print("Adventure in WEBWorld!")
        print("==============================================")
        for i in range(5):
            print("")
        print("==============================================")
        print("Enter player name")
        print("==============================================")
        player_name = input()
        new_player = Player(player_name)

        """play the game"""
# ===============================================================================================
        print("Find the Remote Server before the WEBWorld")
        play_game(new_player)
#================================================================================================
        command=""
        print("would you like to play again? type 'y' to play again or 'q' to exit")
        command = input()
        while command != "y" and command != "q":
            print("invalid input received! Try again!")
            command = input()

        if command == "q":
            print("Exiting Game")
            break





