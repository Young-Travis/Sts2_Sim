class BattleSim:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = []

    def start_battle(self):

        print("Battle started!")
        # Call on_combat_start for relics
        for relic in self.player.relics:
            relic.on_combat_start(self.player)
        for relic in self.enemy.relics:
            relic.on_combat_start(self.enemy)

        while True:
            # Player's turn
            self.player.take_turn(self.enemy)
            if self.enemy.is_dead():
                print("Enemy defeated!")
                break

            # Enemy's turn
            self.enemy.take_turn(self.player)
            if self.player.is_dead():
                print("Player defeated!")
                break

        # Call on_combat_end for relics
        for relic in self.player.relics:
            relic.on_combat_end(self.player)
        for relic in self.enemy.relics:
            relic.on_combat_end(self.enemy)

        print("Battle ended!")