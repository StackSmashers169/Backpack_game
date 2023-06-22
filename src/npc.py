# code written by Victor J Wilson (20094873)
from src.item import Item


class NPC:

    def __init__(self, name: str, dialogue: str, gives_item: bool, damages_you: bool, items: list):
        self.name = name
        self.dialogue = dialogue
        self.gives_item = gives_item
        self.damages_you = damages_you
        self.items = items

    def get_name(self):
        return self.name

    # assigns npcs an item if their gives_item is true.
    def assign_item(self, item: Item):
        self.items.append(item)

    # npcs only have one item at most so just return items[0]
    def give_item(self):
        if not self.gives_item:
            return
        print("got {} from {}".format(self.items[0].name, self.name))
        return self.items[0]

    def read_dialogue(self):
        print(self.dialogue)
