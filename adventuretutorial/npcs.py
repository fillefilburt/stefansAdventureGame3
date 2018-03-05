# npcs described here


class Npc:
    def __init__(self, name, description, alive):
        self.name = name
        self.description = description
        self.alive = alive


class Vix(Npc):
    def __init__(self):
        super().__init__('Vix', 'Vix is a dude', True)

