
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
        
