from typing import Sequence

class BackPack:
    """
    BackPack Class



    ToDo: [X] Instantiate backpack
    ToDo: [X] Add Item
    ToDo: [ ] Remove Item
    ToDo: [ ] List Items
    ToDo: [X] Count items
    ToDo: [ ] in backpack (Search for Item - Student to do)
    ToDo: [X] Sort Items

    """

    def __init__(self, items: Sequence):
        self._backpack = []
        if items is None:
            items = []
        for item in items:
            self._backpack.append(item)
        self.sort()



    def sort(self):
        self._backpack.sort()

    def count(self):
        return self._backpack.count()

    def __len__(self):
        return len(self._backpack)

    def __getitem__(self, index):
        return self._backpack[index]

    def add(self, item):
        if item is not None:
            self._backpack.append(item)
            self.sort()

    def in_backpack(self, item):
        """
        Complete this method using a binary search
        returns -1 or False if not found
        returns position if found
        :param item:
        :return: -1 | False | integer
        """


        return None