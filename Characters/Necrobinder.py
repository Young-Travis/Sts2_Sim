from Base_Char import Player
import Cards.Necrobinder_Cards as Cards

class Necrobinder(Player):
    def __init__(self, health):
        super().__init__(health)
        self.name = "Necrobind"
        self.orb_slots = 0
        self.minion_health = 0