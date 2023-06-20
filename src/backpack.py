

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

    def __init__(self, items: list):
        self._backpack = []
        if items is None:
            items = []
        for item in items:
            self._backpack.append(item)
        self.sort()

    def sort(self):
        self._backpack.sort()

    def count(self):
        return self._backpack.count

    def __len__(self):
        return len(self._backpack)

    def __getitem__(self, index):
        return self._backpack[index]

    def add(self, item):
        if item is not None:
            self._backpack.append(item)
            self.sort()

    def in_backpack(self, item_name):
        """
        Complete this method using a binary search
        returns -1 or False if not found
        returns position if found
        :param item_name:
        :return: -1 | False | integer
        """
        low = 0
        high = len(self._backpack) - 1

        while low <= high:
            mid = (low + high)//2
            mid_item = self._backpack[mid].name

            if mid_item == item_name:
                return mid
            elif mid_item < item_name:
                low = mid + 1
            else:
                high = mid - 1

        return -1

