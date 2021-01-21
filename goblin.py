class Goblin:
    def __init__(self, health = 6, power = 2):
        self.health = health
        self.power = power

    def attack(self, hero):
        hero.health -= self.power

    def status(self, goblin):
            if self.health > 0:
                print(f"You have {self.health} health and {self.power} power.")
    
    def alive(self):
        while self.health > 0:
            return True