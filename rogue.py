from hero import Hero
from random import randrange

class Rogue(Hero):
    def __init__(self, health = 5, power = 5, exp = 0, level = 1, level_next = 25):
        super().__init__(exp, level, level_next)
        self.health = health
        self.power = power
    def attack(self, enemy):
        dodge = randrange(5)
        if dodge != 4:
            enemy.health -= self.power
            self.health += enemy.power
            print(f'You dodged the attack and did {self.power} to the {enemy}.')
        if dodge == 4:
            enemy.health -= self.power
            print(f'You did {self.power} damage to the {enemy}.')