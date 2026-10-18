from Cards.Card_Class import Card

class Strike_Silent(Card):
    def __init__(self):
        super().__init__()
        self.name = "Strike"
        self.energy_cost = 1
        self.base_damage = 6

class Defend_Silent(Card):
    def __init__(self):
        super().__init__()
        self.name = "Defend"
        self.energy_cost = 1
        self.base_block = 5
    
