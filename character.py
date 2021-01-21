from random import randrange
class Character:
    def __init__(self, health=1, power=1):
        self.health = health
        self.power = power
    
    # def __str__(self):
    #     return 
    
    def status(self):
            if self.health > 0:
                print(f"The {self} has {self.health} health and {self.power} power.")
    
    def alive(self):
        if self.health > 0:
            return True

    
    def dead(self):
        if self.health <= 0:
            return print(f'The {self} is dead')

    
    def attack(self, hero):
        hero.health -= self.power
        print(f"The {self} does {self.power} damage to you.")


class Hero(Character):
    def __init__(self, health = 10, power = 5):
        # super().__init__(10, 5)
        self.power = power
        self.health = health
    
    def attack(self, enemy):
        crit = randrange(5)
        if crit == 4:
            enemy.health -= self.power * 2
            print(f"You do {self.power * 2} damage to the {enemy}.")
        elif crit != 4:
            enemy.health -= self.power
            print(f"You do {self.power} damage to the {enemy}.")

    def dead(self):
        if self.health <= 0:
            return print('You are dead!')

    def status(self):
            if self.health > 0:
                print(f"You have {self.health} health and {self.power} power.")

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

class Rogue(Hero):
    def __init__(self, health = 5, power = 5):
        self.health = health
        self.power = power
    def attack(self, enemy):
        dodge = randrange(5)
        if dodge != 4:
            enemy.health -= self.power
            self.health = 1
            print(f'You dodged the attack and did {self.power} to the {enemy}.')
        if dodge == 4:
            enemy.health -= self.power
            print(f'You did {self.power} damage to the {enemy}.')

class Goblin(Character):
    def __init__(self, health = 6, power = 2):
        # super().__init__(6, 2)
        self.power = power
        self.health = health
    
    def __str__(self):
        return "Goblin"

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