# from character import Character, Hero, Goblin, Shadow, Medic, Zombie, Warrior, Priest, Mage, Rogue
from random import randrange
from menu import Menu
from warrior import Warrior
from priest import Priest
from mage import Mage
from rogue import Rogue

# list for make hero
hero = []

main_menu = [
    "Go to the store",
    "Rest at the inn",
    "Explore outside town",
    "Level up",
    "Choose class"
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
        choice = home.get_choice()
        if choice == 3:
            hero.battle()
        if choice == 5:
            pass
        if not hero.alive():
            print("You are dead!")

main()