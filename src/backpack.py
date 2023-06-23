from src.item import Item


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

    #
    def __init__(self, items: list):
        self._backpack = []
        if items is None:
            items = []
        for item in items:
            self._backpack.append(item)
        self.sort()

    # uses the key parameter of python sort to sort objects by item name.
    def sort(self):
        self._backpack.sort(key=lambda item: item.name)

    # the length of the backpack denotes the count
    def __len__(self):
        return len(self._backpack)

    def __getitem__(self, index: int):
        if index >= 0:
            return self._backpack[index]

    def __delitem__(self, index: int):
        del self._backpack[index]

    def add(self, item: Item):
        if item is not None:
            print("You added {} to your backpack".format(item.name))
            self._backpack.append(item)
            self.sort()

    # prints the contents of the backpack to the terminal as an inventory list.
    def print_backpack_items(self):
        if not self._backpack:
            print("backpack is empty")
            return

        print("Current Inventory List:")
        for item in self._backpack:
            print(item.name)

    # uses binary search to find an item in the backpack using the item_name as a reference.
    def in_backpack(self, item_name: str):
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
            mid = (low + high) // 2
            mid_item = self._backpack[mid].name

            if mid_item == item_name:
                return mid
            elif mid_item < item_name:
                low = mid + 1
            else:
                high = mid - 1

        return -1
