from Buffs.Buff_Class import Buff

class Strength(Buff):
    def __init__(self, amount, duration):
        super().__init__(duration)
        self.amount = amount

class Dexterity(Buff):
    def __init__(self, amount, duration):
        super().__init__(duration)
        self.amount = amount