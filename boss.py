from character import Character

class Boss(Character):
    def __init__(self, level = 1, health = 100, power = 10):
        self.health = health
        self.power = power
        self.level = level
    
    def __str__(self):
        return "Abomination"