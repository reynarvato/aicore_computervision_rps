import numpy as np
import random

class RPS():
    def __init__(self):
        self.player_img = None # take img parameter
        self.player_guess = int
        self.computer_guess = int

        self.player_score = 0
        self.computer_score = 0
        self.HAND = ["rock","paper","scissors"]

    def compare_hands(self):
        while(True):
            self.player_guess = int(input("Enter guess: 0 = Rock, 1 = Paper, 2 = Scissors\n"))
            if self.player_guess>-2 and self.player_guess<3:
                break

        self.computer_guess = random.randint(0,2)

        print("Player={}\nComputer={}".format(self.HAND[self.player_guess],self.HAND[self.computer_guess]))

        # z = x-y
        z = self.player_guess-self.computer_guess

        if z == -2:
            z = 1
        elif z== 2:
            z = -1

        if z == 0:
            print("draw")
            return "draw"
        elif z == 1: 
            print("win")
            return "win"
        elif z == -1:
            print("lose")
            return "lose"

    def tally(self,outcome):
        if outcome == "win":
            self.player_score += 1
            self.computer_score += 1
        if self.player_score > 5:
            print("Congratulations, player wins!")
        elif self.computer_score > 5:
            print("Nice try, computer wins!")

game = RPS()
while(True):
    outcome = game.compare_hands()
    game.tally(outcome)
