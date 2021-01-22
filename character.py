from random import randrange

class Character:
    def __init__(self, health=1, power=1):
        self.health = health
        self.power = power
    
    # def __str__(self):
    #     return 
    
    def status(self):
        if self.is_alive():
            print(f"The {self} has {self.health} health and {self.power} power.")
    
    def is_alive(self):
        return self.health > 0

    
    def death_message(self):
        print(f'The {self} is dead')

    
    def attack(self, hero):
        hero.health -= self.power
        print(f"The {self} does {self.power} damage to you.")