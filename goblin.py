from character import Character

class Goblin(Character):
    def __init__(self, health = 6, power = 2):
        # super().__init__(6, 2)
        self.power = power
        self.health = health
    
    def __str__(self):
        return "Goblin"