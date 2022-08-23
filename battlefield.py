from dinosaur import Dinosaur
from robot import Robot 


class Battlefield:

    def __init__(self):
        self.dinosaur = Dinosaur("rex")
        self.robot = Robot("Square2")
    
    def run_game(self):
        self.display_welcome()
        self.battle()

    def display_welcome(self):
        print("welcome to robot vs dinosaur. Who will be the winner?")

    def battle(self):
        self.robot.attack(self.dinosaur)
        self.dinosaur.attack(self.robot)

    def display_winner(self):
        pass

