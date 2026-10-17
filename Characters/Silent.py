from Base_Char import Player
import Cards.Silent_Cards as Cards

class Silent(Player):
    def __init__(self, health):
        super().__init__(health)
        self.name = "Silent"
        self.orb_slots = 0
        self.minion_health = 0
