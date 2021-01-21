class Hero:
    def __init__(self, health = 10, power = 5):
        self.health = health
        self.power = power

    def attack(self, goblin):
        goblin.health -= self.power

    def status(self, hero):
        if self.health > 0:
            print(f"You have {self.health} health and {self.power} power.")
    
    def alive(self):
        while self.health > 0:
            return True
