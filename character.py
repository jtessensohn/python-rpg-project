from random import randrange

class Character:
    def __init__(self, level = 1, health=1, power=1):
        self.health = health
        self.power = power
        self.level = level
    
    # def __str__(self):
    #     return 
    
    def status(self):
        if self.is_alive():
            print(f"The {self} has {self.health} health and {self.power} power.")
    
    def is_alive(self):
        return self.health > 0

    
    def death_message(self):
        print(f'The {self} is dead')

    
    def attack(self, hero):
        hero.health -= self.power
        print(f"The {self} does {self.power} damage to you.")
    
    def enemy_level_up(self, hero):
        if self.level < hero.level:
            self.level = hero.level
            # print(f"It seems the enemies around the town have gotten stronger too...")
            self.health += round(self.health * .15)
            self.health += round(self.health * .45)
        # if self.exp >= self.level_next:
        #     self.level += 1
        #     self.exp = self.exp - self.level_next
        #     self.level_next = round(self.level_next * 1.25)
        #     print(f'Level up! You are now level {self.level}. You earned {round(self.health * .33)} health and {round(self.power * .75)} power!')
        #     self.health += round(self.health * .33)
        #     self.power += round(self.power * .75)