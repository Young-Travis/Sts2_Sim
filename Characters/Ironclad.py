from Base_Char import Player
import Cards.Ironclad_Cards as Cards

class Ironclad(Player):
    def __init__(self, health):
        super().__init__(health)
        self.name = "Ironclad"
        self.orb_slots = 0
        self.minion_health = 0

        self.generate_starting_deck()
        self.alphabetical_sort_deck()

    def generate_starting_deck(self):
        for i in range(5):
            self.deck.append(Cards.Strike_Iron())
            if i < 4:
                self.deck.append(Cards.Defend_Iron())
        self.deck.append(Cards.Bash())
