from Characters.Ironclad import Ironclad
from Characters.Defect import Defect
from Orbs.Orbs import Lightning_Orb, Frost_Orb, Dark_Orb, Plasma_Orb
import random


def start_game():
    random.seed(0)
    print("Welcome to the game!")
    player = Defect(80)
    print(f"You are playing as {player.name} with {player.current_health}/{player.max_health} health.")
    print(f"Your starting deck has {len(player.deck)} cards.")
    for card in player.deck:
        print(f"- {card.name} (Cost: {card.energy_cost})")
    for i in range(5):
        orb_type = random.choice([Lightning_Orb, Frost_Orb, Dark_Orb, Plasma_Orb])
        player.channel_orb(orb_type(player))
    print(player.orbs)
    print(player.relics)

if __name__ == "__main__":
    start_game()