# code written by Victor J Wilson (20094873)

class NPC:

    def __init__(self, name: str, dialogue: str, gives_item: bool, damages_you: bool):
        self.name = name
        self.dialogue = dialogue
        self.gives_item = gives_item
        self.damages_you = damages_you

    def get_name(self):
        return self.name

    def read_dialogue(self, option: int):
        print(self._lines[option])





