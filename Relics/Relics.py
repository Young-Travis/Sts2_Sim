from Relics.Relic_Class import Relic

class Burning_Blood(Relic):
    def __init__(self, holder):
        super().__init__(holder)
        self.name = "Burning Blood"

    def on_combat_end(self, character):
        print("Heals 6 HP")

class Cracked_Core(Relic):
    def __init__(self, holder):
        super().__init__(holder)
        self.name = "Cracked Core"
    
    def on_combat_start(self, character):
        print("Channels 1 lightning")