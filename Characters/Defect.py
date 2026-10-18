from Characters.Base_Char import Player
import Cards.Defect_Cards as Cards
import Relics.Relics as relics

class Defect(Player):
    def __init__(self, health):
        super().__init__(health)
        self.name = "Defect"
        self.orb_slots = 3
        self.minion_health = 0

        self.generate_starting_deck()
        self.alphabetical_sort_deck()
        self.get_starting_relic()

    def generate_starting_deck(self):
        for _ in range(4):
            self.deck.append(Cards.Strike_Defect())
            self.deck.append(Cards.Defend_Defect())
        self.deck.append(Cards.Zap())
        self.deck.append(Cards.Dualcast())
    
    def get_starting_relic(self):
        self.relics.append(relics.Cracked_Core(self))