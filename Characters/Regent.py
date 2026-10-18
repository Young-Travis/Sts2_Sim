from Characters.Base_Char import Player
import Cards.Regent_Cards as Cards

class Regent(Player):
    def __init__(self, health):
        super().__init__(health)
        self.name = "Regent"
        self.orb_slots = 0
        self.minion_health = 0