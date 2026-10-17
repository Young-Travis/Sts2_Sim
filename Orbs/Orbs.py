from Orbs.Orb_Class import orb

class Lightning_Orb(orb):
    def __init__(self, player):
        super().__init__(player)
        self.name = "Lightning Orb"

    def on_evoke(self):
        print("Lightning Orb evoked!")

class Frost_Orb(orb):
    def __init__(self, player):
        super().__init__(player)
        self.name = "Frost Orb"

    def on_evoke(self):
        print("Frost Orb evoked!")

class Dark_Orb(orb):
    def __init__(self, player):
        super().__init__(player)
        self.name = "Dark Orb"

    def on_evoke(self):
        print("Dark Orb evoked!")

class Plasma_Orb(orb):
    def __init__(self, player):
        super().__init__(player)
        self.name = "Plasma Orb"

    def on_evoke(self):
        print("Plasma Orb evoked!")
        