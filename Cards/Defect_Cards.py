from Card_Class import Card
from Orbs.Orbs import Lightning_Orb, Frost_Orb, Dark_Orb, Plasma_Orb

class Strike_Defect(Card):
    def __init__(self):
        super().__init__()
        self.name = "Strike"
        self.energy_cost = 1
        self.base_damage = 6

    def On_Play(self):
        print("Strike played! Dealing 6 damage to the enemy.")

class Defend_Defect(Card):
    def __init__(self):
        super().__init__()
        self.name = "Defend"
        self.energy_cost = 1
        self.base_block = 5

    def On_Play(self):
        print("Defend played! Gaining 5 block.")

class Zap(Card):
    def __init__(self):
        super().__init__()
        self.name = "Zap"
        self.energy_cost = 1

    def On_Play(self):
        print("Zap played! Channeling 1 Lightning Orb.")
        self.player.channel_orb(Lightning_Orb(self.player))

class Dualcast(Card):
    def __init__(self):
        super().__init__()
        self.name = "Dualcast"
        self.energy_cost = 1

    def On_Play(self):
        print("Dualcast played! Evoke next orb twice.")