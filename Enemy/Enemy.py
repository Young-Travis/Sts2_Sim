class enemy:
    def __init__(self, max_health):
        self.name = "No Enemy Selected"
        self.max_health = max_health
        self.current_health = self.max_health
        self.block = 0
        self.dead = False

        def take_damage(self, amount):
            if self.block > 0:
                if amount <= self.block:
                    self.block -= amount
                    print(f"{self.name} blocked {amount} damage. Remaining block: {self.block}")
                    return
                else:
                    amount -= self.block
                    print(f"{self.name} blocked {self.block} damage. Remaining damage: {amount}")
                    self.block = 0
            self.current_health -= amount
            print(f"{self.name} took {amount} damage")
            if self.current_health < 0:
                self.current_health = 0
                print(f"{self.name} has died")
                self.dead = True
            self.print_health()

        def is_dead(self):
            return self.dead