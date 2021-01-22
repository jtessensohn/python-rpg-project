from random import randrange
from hero import Hero

class Warrior(Hero):
    def __init__(self, health = 15, power = 4):
        self.health = health
        self.power = power
    def attack(self, enemy):
        crit = randrange(5)
        if crit == 4:
            enemy.health -= self.power * 2.5
            print(f"You do {self.power * 2.5} damage to the {enemy}.")
        elif crit != 4:
            enemy.health -= self.power
            print(f"You do {self.power} damage to the {enemy}.")