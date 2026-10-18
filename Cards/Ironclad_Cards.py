from Cards.Card_Class import Card

class Strike_Iron(Card):
    def __init__(self):
        super().__init__()
        self.name = "Strike"
        self.energy_cost = 1
        self.base_damage = 6

class Defend_Iron(Card):
    def __init__(self):
        super().__init__()
        self.name = "Defend"
        self.energy_cost = 1
        self.base_block = 5

class Bash(Card):
    def __init__(self):
        super().__init__()
        self.name = "Bash"
        self.energy_cost = 2
        self.base_damage = 8

    def On_Play(self):
        print("Bash played! Applying 2 Vulnerable to the enemy.")