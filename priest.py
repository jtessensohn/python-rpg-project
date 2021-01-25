from random import randrange
from hero import Hero

class Priest(Hero):
    def __init__(self, max_health = 6, health = 6, power = 3, exp = 0, level = 1, level_next = 25, earned_gold = 0, total_gold = 0):
        super().__init__(exp, level, level_next, earned_gold, total_gold)
        self.health = health
        self.power = power
        self.max_health = max_health

    def attack(self, enemy):
        heal = randrange(5)
        if heal == 4:
            enemy.health -= self.power
            print(f"You do {self.power} damage to the {enemy}.")
        elif heal != 4:
            enemy.health -= self.power
            self.health += self.power
            print(f"You do {self.power} damage to the {enemy} and healed yourself for {self.power} health.")