from random import randrange
from hero import Hero


class Mage(Hero):
    def __init__(self, max_health = 5, health = 5, power = 7, exp = 0, level = 1, level_next = 25, earned_gold = 0, total_gold = 0):
        super().__init__(exp, level, level_next, earned_gold, total_gold)
        self.health = health
        self.power = power
        self.max_health = max_health
    def attack(self, enemy):
        crit = randrange(3)
        if crit == 2:
            enemy.health -= self.power * 5
            print(f"You do {self.power * 5} damage to the {enemy}.")
        elif crit != 2:
            enemy.health -= self.power
            print(f"You do {self.power} damage to the {enemy}.")