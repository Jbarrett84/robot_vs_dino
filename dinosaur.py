class Dinosaur:
   
    def __init__(self, name):
        self.name = name 
        self.attack_power = 75
        self.health = 100 

    def attack(self, robot):
        robot.health -= self.attack_power
        print(f'{robot.name} was attacked by {self.name} using {self.attack_power} causing confusion and leaving the {robot.health} health')