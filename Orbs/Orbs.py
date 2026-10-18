from Orbs.Orb_Class import orb

class Lightning_Orb(orb):
    def __init__(self, player):
        super().__init__(player)
        self.name = "Lightning Orb"
        self.damage = 3

    def on_evoke(self):
        print("Lightning Orb evoked!")
    
    def on_turn_end(self):
        print("Lightning Orb deals 3 damage to the enemy at the end of the turn.")

class Frost_Orb(orb):
    def __init__(self, player):
        super().__init__(player)
        self.name = "Frost Orb"

    def on_evoke(self):
        print("Frost Orb evoked!")

    def on_turn_end(self):
        print("Frost Orb gains 2 block for the player at the end of the turn.")

class Dark_Orb(orb):
    def __init__(self, player):
        super().__init__(player)
        self.name = "Dark Orb"

    def on_evoke(self):
        print("Dark Orb evoked!")

    def on_turn_end(self):
        print("Dark Orb gains evoke damage")

class Plasma_Orb(orb):
    def __init__(self, player):
        super().__init__(player)
        self.name = "Plasma Orb"

    def on_evoke(self):
        print("Plasma Orb evoked!")
    
    def on_turn_start(self):
        print("Plasma orb generates 1 energy per turn")

class Glass_Orb(orb):
    def __init__(self, player):
        super().__init__(player)
        self.name = "Glass Orb"

    def on_evoke(self):
        print("Glass Orb evoked!")
    
    def on_turn_end(self):
        print("Glass orb deals damage to all enemies and loses 1 damage")
        