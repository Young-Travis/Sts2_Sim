class Relic:
    def __init__(self, holder):
        self.name = ""
        self.holder = holder
    
    def on_combat_start(self, player):
        pass
    
    def on_combat_end(self, player):
        pass