# TODO impose health maximum in regards to healing at the tavern
# add more growth through money to spend at the shop
# add item use functionality
# add boss
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
    "Go to the store",
    "Rest at the Tavern",
    "Explore outside town",
    "Visit the mentor",
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
    home = Menu("Please choose an Option: \n", main_menu)
    # types = Menu("Please choose your class: ", main_menu)
    while True:
        choice = home.get_choice()
        if choice == 1:
            pass
        if choice == 2:
            hero.rest()
        if choice == 3:
            hero.battle()
        if choice == 4:
            hero.level_up()
        if choice == 5:
            print('Maybe someone more capable will take the challenge')
            break
        if not hero.is_alive:
            print("You are dead!")

main()