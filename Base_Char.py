class Player:
    def __init__(self, max_health):
        self.name = "No Player Selected"
        self.max_health = max_health
        self.current_health = self.max_health
        self.block = 0
        self.stars = 0
        self.orb_slots = 0
        self.minion_health = 0
        self.orbs = []
        self.deck = []
        self.relics = []
        self.afflictions = []

    def generate_starting_deck(self):
        pass        

    def get_starting_relic(self):
        pass

    def alphabetical_sort_deck(self):
        self.deck.sort(key=lambda card: card.name)

    def add_card(self, card):
        self.deck.append(card)

    def remove_card(self, card):
        if card in self.deck:
            self.deck.remove(card)

    def print_health(self):
        print(f"{self.name} Health: {self.current_health}/{self.max_health}")

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
        self.print_health()

    def gain_max_health(self, amount):
        self.max_health += amount
        self.current_health += amount
        print(f"{self.name} gained {amount} max health")
        self.print_health()

    def heal(self, amount):
        self.current_health += amount
        if self.current_health > self.max_health:
            self.current_health = self.max_health
        print(f"{self.name} healed {amount} health")
        self.print_health()

    def gain_block(self, amount):
        self.block += amount
        print(f"{self.name} gained {amount} block. Total block: {self.block}")
    
    def lose_block(self):
        self.block = 0

    def give_relic(self, relic):
        self.relics.append(relic)
        print(f"{self.name} received relic: {relic.name}")

    def channel_orb(self, orb):
        if self.orb_slots == 0:
            self.orb_slots = 1
        self.orbs.append(orb)
        if len(self.orbs) > self.orb_slots:
            evoked_orb = self.orbs[0]
            print(f"{self.name} evoked {evoked_orb.name} due to exceeding orb slots.")
            self.evoke_orb(evoked_orb)
    
    def evoke_orb(self, orb):
        orb.on_evoke()
        self.orbs.pop(0)

    def gain_buff(self, buff):
        if any(isinstance(buff, type(buff)) for item in afflictions):
            print(f"{self.name} already has {buff.__class__.__name__}")
        