from random import randrange
from character import Character

class Medic(Character):
    def __init__(self, health = 10, power = 2):
        self.health = health
        self.power = power
    
    def attack(self, hero):
        heal = randrange(5)
        if heal == 4:
            hero.health -= self.power
            self.health += 2
            print(f"{self} does {self.power} damage to you and healed for 2!")
        elif heal != 4:
            hero.health -= self.power
            print(f"{self} does {self.power} damage to the you.")
    def __str__(self):
        return "Medic"