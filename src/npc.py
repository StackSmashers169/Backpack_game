# code written by Victor J Wilson (20094873)

class NPC:

    def __init__(self, name: str, dialogues: list, action: str):
        self.name = name
        self._lines = []
        if dialogues is None:
            dialogues = []
        for dialogue in dialogues:
            self._lines.append(dialogue)
        self.action = action
        self._dialogue_option = False

    def change_dialogue_options(self, choice: str):
        if str == "yes" or "Yes":
            self._dialogue_option = True

    def read_dialogue(self, option: int):
        print(self._lines[option])





