from random import randrange
from hero import Hero

class Priest(Hero):
    def __init__(self, health = 6, power = 3):
        self.health = health
        self.power = power

    def attack(self, enemy):
        heal = randrange(5)
        if heal == 4:
            enemy.health -= self.power
            print(f"You do {self.power} damage to the {enemy}.")
        elif heal != 4:
            enemy.health -= self.power
            self.health += self.power
            print(f"You do {self.power} damage to the {enemy} and healed yourself for {self.power} health.")