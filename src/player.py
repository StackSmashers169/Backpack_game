# code by Victor J Wilson(20094873)


from backpack import BackPack


class Player:

    def __init__(self, name):
        self.name = name
        self.is_alive = True
        self.data = 50  # data represents HP for this character or more precisely 50b.
        self.items = []
        self.backpack = BackPack(self.items)
        self.position = []

    # saves the player's position on the map
    def save_position(self, x_coordinate, y_coordinate):
        pass

    # searches location for an item
    def search_location(self):
        pass

    # if an NPC(s) exists in this location you can talk to them.
    def talk_to_npc(self):
        pass

    # called if player triggers a gain_hp tile
    def gain_hp(self):
        pass

    # called if player triggers a lose_hp tile

    def lose_hp(self):
        pass


