# code by Victor J Wilson(20094873)

from typing import Sequence

from backpack import BackPack
class Player:

    def __init__(self, name, items: Sequence):
        self.name = name
        self.IsAlive = true
        self.hp = 50  # default HP is 50


        if items is None:
            self.backpack = BackPack()


