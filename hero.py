from random import randrange
from character import Character
from goblin import Goblin
from medic import Medic
from shadow import Shadow
from zombie import Zombie

ENEMY_CLASSES = {
    0: Goblin,
    1: Medic,
    2: Shadow,
    3: Zombie
}

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
    
    def battle(self):
        enemy_roll = randrange(4)
        enemy = ENEMY_CLASSES[enemy_roll]()
        while enemy.is_alive() and self.is_alive():
            self.status()
            enemy.status()
            print()
            print("What do you want to do?")
            print(f"1. fight {enemy}")
            print("2. do nothing")
            print("3. flee")
            print("> ",)
            user_input = input()
            if user_input == "1":
                # Hero attacks goblin
                self.attack(enemy)
                enemy.attack(self)
                print('\n')
                if enemy.is_alive() != True:
                    enemy.death_message()
                if self.is_alive() !=True:
                    self.death_message()
                enemy.is_alive()
            elif user_input == "2":
                enemy.attack(self)
                if enemy.is_alive() != True:
                    enemy.death_message()
                # if self.is_alive() !=True:
                #     self.dead()
            elif user_input == "3":
                print("Goodbye.")
                break
            else:
                print("Invalid input %r" % user_input)