from character import Character, Hero, Goblin, Medic, Shadow, Zombie
from random import randrange
from town import create_hero

def battle():
    my_hero = hero_choice
    enemy = randrange(4)
    if enemy == 0:
        enemy = Goblin()
    elif enemy == 1:
        enemy = Medic()
    elif enemy == 2:
        enemy = Shadow()
    elif enemy == 3:
        enemy = Zombie()
    while enemy.alive() and my_hero.alive():
        my_hero.status()
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
            my_hero.attack(enemy)
            enemy.attack(my_hero)
            print('\n')
            if enemy.alive() != True:
                enemy.dead()
            if my_hero.alive() !=True:
                my_hero.dead()
            enemy.alive()
        elif user_input == "2":
            enemy.attack(my_hero)
            if enemy.alive() != True:
                enemy.dead()
            if my_hero.alive() !=True:
                my_hero.dead()
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)
