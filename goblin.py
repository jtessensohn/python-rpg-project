from character import Character

class Goblin(Character):
    def __init__(self, level = 1, health = 6, power = 2):
        self.power = power
        self.health = health
        self.level = level
    
    def __str__(self):
        return "Goblin"