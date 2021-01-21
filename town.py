
from character import Character, Hero, Goblin, Shadow, Medic, Zombie, Warrior, Priest, Mage, Rogue
from menu import Menu
from random import randrange

# list for make hero
hero = []

main_menu = [
    "Go to the store",
    "Rest at the inn",
    "Explore outside town",
    "Level up",
    "Choose class"
]

create_hero = [
    "Warrior",
    "Priest",
    "Mage",
    "Rogue"
]
def hero_create():
    hero_choice = input("Please select your class " + str(create_hero) + " ")
    if hero_choice == Warrior:
        hero_choice == Warrior()
        return hero_choice
    elif hero_choice == Priest:
        hero_choice == Priest()
        return hero_choice
    elif hero_choice == Mage:
        hero_choice == Mage()
        return hero_choice
    elif hero_choice == Rogue:
        hero_choice == Rogue()
        return hero_choice
    
def main():
    home = Menu("Please choose an Option ", main_menu)
    types = Menu("Please choose your class: ", main_menu)
    while True:
        choice = home.get_choice()
        if choice == 3:
            battle()
        if choice == 5:
            pass

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


hero_choice = hero_create()
main()