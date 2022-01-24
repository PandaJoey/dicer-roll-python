"""
As the name of the program suggests, we will be imitating a rolling dice. 
This is one of the interesting python projects and will generate a random 
number each dice the program runs, and the users can use the dice 
repeatedly for as long as he wants. When the user rolls the dice, 
the program will generate a random number between 1 and 6     (as on a standard dice).
The number will then be displayed to the user. It will also ask users if they 
would like to roll the dice again. The program should also include a function 
that can randomly grab a number within 1 to 6 and print it. This beginner-level 
python projects will help build a strong foundation for fundamental programming 
concepts.
"""

import random

class DiceSimulator:
    """
    Dice Roll Simulator
    """ 
    
    def __init__(self):
        self.dice = random.randint(1, 6)
        self.play = " "
        self.min = 1
        self.max = 6
    
    def roll(self):
     
        play_game = True
        
        while play_game:
            play_more = input("Would you like to roll again, y or n: ")
            if play_more == "y":
                self.play = int(input("How many dice would you like to roll?: "))
                total = 0
                for item in range(self.play):
                    dice = list(range(self.play))
                    dice[item] = random.randint(self.min, self.max)
                    total += dice[item]
                    print(dice[item])
                print(f"total is: {total}")  
            else:
                print("thanks for playing")
                break
                
play = DiceSimulator()
play.roll()
        