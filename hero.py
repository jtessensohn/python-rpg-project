from random import randrange
from character import Character
from goblin import Goblin
from medic import Medic
from shadow import Shadow
from zombie import Zombie
from boss import Boss

ENEMY_CLASSES = {
    0: Goblin,
    1: Medic,
    2: Shadow,
    3: Zombie
}

class Hero(Character):
    def __init__(self, exp, max_health = 10, health = 10, power = 5, level = 1, level_next = 25, earned_gold = 0, total_gold = 0):
        self.power = power
        self.max_health = max_health
        self.health = health
        self.exp = 0
        self.level = level
        self.level_next = level_next
        self.earned_gold = earned_gold
        self.total_gold = total_gold
    
    def attack(self, enemy):
        crit = randrange(5)
        if crit == 4:
            enemy.health -= self.power * 2
            print(f"You do {self.power * 2} damage to the {enemy}.")
        elif crit != 4:
            enemy.health -= self.power
            print(f"You do {self.power} damage to the {enemy}.")

    def death_message(self):
        print('You are dead!')
        quit()

    def status(self):
            if self.health > 0:
                print(f"You have {self.health} health and {self.power} power.")
    
    def battle(self):
        enemy_roll = randrange(4)
        enemy = ENEMY_CLASSES[enemy_roll]()
        self.get_gold(enemy)
        if enemy.level < self.level:
            level_diff = (self.level - enemy.level)
            enemy.level = self.level
            enemy.health += round((enemy.health * .85) * level_diff)
            enemy.power += round((enemy.power * .70) * level_diff)
        while enemy.is_alive() and self.is_alive():
            self.status()
            enemy.status()
            print()
            print("What do you want to do?")
            print(f"1. fight {enemy}")
            print("2. do nothing")
            print("3. flee")
            user_input = input("> ")
            if user_input == "1":
                # Hero attacks goblin
                self.attack(enemy)
                enemy.attack(self)
                print('\n')
                if enemy.is_alive() != True:
                    enemy.death_message()
                    self.get_exp()
                    # self.get_gold(enemy)
                if self.is_alive() !=True:
                    self.death_message()
                    quit()
                enemy.is_alive()
            elif user_input == "2":
                enemy.attack(self)
                if enemy.is_alive() != True:
                    enemy.death_message()
                if self.is_alive() !=True:
                    self.death_message()
                    quit()
            elif user_input == "3":
                
                print(f"Your display of cowardice impressed the {enemy} long enough for you to escape.")
                break
            else:
                print("Invalid input %r" % user_input)

    def boss_battle(self):
        enemy = Boss()
        print("\nBefore you stands a creature of unknown origin. \nYou struggle to make out its composition \nbut by the stench alone you know that it must be dealt with.\n\n")
        if enemy.level < self.level:
            level_diff = (self.level - enemy.level)
            enemy.level = self.level
            enemy.health += round((enemy.health * .45) * level_diff)
            enemy.power += round((enemy.power * .65) * level_diff)
        while enemy.is_alive() and self.is_alive():
            print("\n")
            self.status()
            enemy.status()
            print()
            print("What do you want to do?")
            print(f"1. fight {enemy}")
            print("2. do nothing")
            print("3. flee")
            user_input = input("> ")
            if user_input == "1":
                # Hero attacks goblin
                self.attack(enemy)
                enemy.attack(self)
                print('\n')
                if enemy.is_alive() != True:
                    enemy.death_message()
                    self.get_exp()
                if self.is_alive() !=True:
                    self.death_message()
                    quit()
                enemy.is_alive()
            elif user_input == "2":
                enemy.attack(self)
                if enemy.is_alive() != True:
                    enemy.death_message()
                if self.is_alive() !=True:
                    self.death_message()
                    quit()
            elif user_input == "3":
                print("Goodbye.")
                break
            else:
                print("Invalid input %r" % user_input)

    def rest(self):
        self.health = self.max_health
        print(f"You spend some time at the tavern.")
        print(f"You emerge from the dank tavern hall feeling better than before")
        print(f"You have now have {self.health} health.")

    def get_exp(self):
        self.exp += self.power * 2
        print(f'You earned {self.power * 2} experience points!')
        print(f'You have {self.exp} experience points in total')
        if self.exp < self.level_next:
            print(f'You need {self.level_next - self.exp} more experience points to level.')
        elif self.exp >= self.level_next:
            print(f'You have enough experience to level up! Visit the mentor in town.')
    
    def level_up(self):
        if self.exp >= self.level_next:
            self.level += 1
            self.exp = self.exp - self.level_next
            self.level_next = round(self.level_next * 1.25)
            print(f'Level up! You are now level {self.level}. You earned {round(self.max_health * .33)} health and {round(self.power * .75)} power!')
            print(f'It seems the enemies around town are growing in strength as well...')
            self.max_health += round(self.max_health * .33)
            self.power += round(self.power * .75)

    def get_gold(self, enemy_bounty):
        self.earned_gold += enemy_bounty.health *.5
        self.total_gold += self.earned_gold
        print(f"You'll earn {self.earned_gold} gold for this bounty for a total of {self.total_gold} in your wallet.")

    def spend_gold(self):
        self.total_gold -= (round(self.total_gold * .33))
        print(f"You spent {round(self.total_gold * .33)} gold in the tavern.")