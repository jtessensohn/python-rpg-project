from character import Character

class Zombie(Character):
    def __init__(self, health = 10, power = 2):
        self.health = health
        self.power = power

    def alive(self):
        while self.health > -15:
            return True

    def __str__(self):
            return "Zombie"

    def status(self):
        if self.health > -15:
            print(f"The {self} has {self.health} health and {self.power} power.")