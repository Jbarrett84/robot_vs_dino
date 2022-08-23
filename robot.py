from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 80
        self.weapon = Weapon("nunchucks")
    
    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power  
        print(f'{dinosaur.name} was attacked by {self.name} using {self.weapon} causing pain and leaving the {dinosaur.health} health ')
        
