# code written by Victor J Wilson (20094873)
from item import Item

class NPC:

    def __init__(self, name: str, dialogue: str, gives_item: bool, damages_you: bool, items: list):
        self.name = name
        self.dialogue = dialogue
        self.gives_item = gives_item
        self.damages_you = damages_you
        self.items = items

    def get_name(self):
        return self.name

    def add_item(self, item: Item):
        self.items.append(item)

    # npcs only have one item at most so just return items[0]
    def give_item(self):
        if self.gives_item:
            return self.items[0]

    def read_dialogue(self, option: int):
        pass







