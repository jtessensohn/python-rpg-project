from random import randrange
from character import Character

class Shadow(Character):
    def __init__(self, level = 1, health = 1, power = 1):
        self.health = health
        self.power = power
        self.level = level

    def attack(self, hero):
        dodge = randrange(5)
        if dodge != 4:
            hero.health -= self.power
            self.health = 1
            print(f'The {self} dodged your attack and did {self.power} to you!')
        if dodge == 4:
            hero.health -= self.power
            print(f'The {self} did {self.power} damage to you.')

    def __str__(self):
            return "Shadow"