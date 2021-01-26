# dear god do some number tuning

from random import randrange
from menu import Menu
from warrior import Warrior
from priest import Priest
from mage import Mage
from rogue import Rogue
from goblin import Goblin
from medic import Medic
from zombie import Zombie
from shadow import Shadow
from character import Character


main_menu = [
    "Rest at the Tavern",
    "Explore outside town",
    "Visit the mentor",
    "Fight the boss",
    "Retire the mantle"
]

HERO_CLASSES = {
    "Warrior": Warrior,
    "Priest": Priest,
    "Mage": Mage,
    "Rogue": Rogue
}
def hero_create():
    print(list(HERO_CLASSES.keys()))
    hero_choice = input("Please select your class: ")
    selected_class = HERO_CLASSES[hero_choice]
    return selected_class()
    
def main():
    hero = hero_create()
    home = Menu("Please choose an Option: ", main_menu)
    # types = Menu("Please choose your class: ", main_menu)
    while True:
        # print(hero.status)
        print("\n")
        choice = home.get_choice()
        if choice == 1:
            hero.rest()
            hero.spend_gold()
        elif choice == 2:
            hero.battle()
        elif choice == 3:
            hero.level_up()
        elif choice == 4:
            hero.boss_battle()
        elif choice == 5:
            print('Maybe someone more capable will take the challenge')
            break

main()