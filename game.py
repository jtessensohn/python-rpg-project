# TODO add item use functionality
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
    # enemies = Character()
    home = Menu("Please choose an Option: ", main_menu)
    # types = Menu("Please choose your class: ", main_menu)
    while True:
        print("\n")
        choice = home.get_choice()
        battle_count = 0
        # if choice == 1:
        #     pass
        if choice == 1:
            hero.rest()
            hero.spend_gold()
        elif choice == 2:
            hero.battle()
            battle_count += 1
            # if battle_count == 2:
            #     print("You have spotted the boss, prepare to fight!")
        elif choice == 3:
            hero.level_up()
        elif choice == 4:
            hero.boss_battle()
        elif choice == 5:
            print('Maybe someone more capable will take the challenge')
            break

main()