# code written by Victor J Wilson

# the item class, each item has a name and default count value of 1.
class Item:

    def __init__(self, name: str, id: int):
        self.name = name
        self.count = 1
        self.id = id


