class Card:
    def __init__(self):
        '''
        self.name = ""
        self.display_name = ""
        self.energy_cost = 0
        '''

        self.upgraded = False

        def On_Upgrade(self):
            self.display_name += "+"

        def On_Play(self):
            pass