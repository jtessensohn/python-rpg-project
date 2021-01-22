from random import randrange
from hero import Hero


class Mage(Hero):
    def __init__(self, health = 5, power = 7):
        self.health = health
        self.power = power
    def attack(self, enemy):
        crit = randrange(3)
        if crit == 2:
            enemy.health -= self.power * 5
            print(f"You do {self.power * 5} damage to the {enemy}.")
        elif crit != 2:
            enemy.health -= self.power
            print(f"You do {self.power} damage to the {enemy}.")