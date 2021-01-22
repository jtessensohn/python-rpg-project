from random import randrange
from character import Character

class Shadow(Character):
    def __init__(self, health = 1, power = 1):
        self.health = health
        self.power = power

    def attack(self, hero):
        dodge = randrange(10)
        if dodge != 9:
            hero.health -= self.power
            self.health = 1
            print(f'The {self} dodged your attack and did {self.power} to you!')
        if dodge == 9:
            hero.health -= self.power
            print(f'The {self} did {self.power} damage to you.')

    def __str__(self):
            return "Shadow"