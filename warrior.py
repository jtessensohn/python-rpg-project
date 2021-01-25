from random import randrange
from hero import Hero

class Warrior(Hero):
    def __init__(self, max_health = 15, health = 15, power = 4, exp = 0, level = 1, level_next = 25, earned_gold = 0, total_gold = 0):
        super().__init__(exp, level, level_next, earned_gold, total_gold)
        self.health = health
        self.power = power
        self.max_health = max_health
        
    def attack(self, enemy):
        crit = randrange(5)
        if crit == 4:
            enemy.health -= self.power * 3.5
            print(f"You do {self.power * 3.5} damage to the {enemy}.")
        elif crit != 4:
            enemy.health -= self.power
            print(f"You do {self.power} damage to the {enemy}.")