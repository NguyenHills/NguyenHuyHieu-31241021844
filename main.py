#Bonus the game "Oan tu xi"

from random import randint
#Choose Keo Bua Bao


player = input("Choose Keo Bua Bao : ")
print("You choose: " + str(player))

computer=randint(0,2)
if computer == 0:
    computer = "Keo"
if computer == 1:
        computer = "Bua"
if computer == 2:
        computer = "Bao"
print("Computer Choose: " + str(computer))
print("----------------------------------------------------------")
if computer == player:
    print("Draw")
    print("Do you want to play again?")
else:
    if player == "Keo":
        if computer == "Bua":
            print("Lose")
            print("Do you want to play again?")
        else:
            print("Win")
            print("Congratulations! Can you give me high score?")
    elif player == "Bua":
        if computer == "Bao":
            print("Lose")
            print("Do you want to play again?")
        else:
            print("Win")
            print("Congratulations! Can you give me high score?")
    elif player == "Bao":
        if computer == "Keo":
            print("Lose")
            print("Do you want to play again?")
        else:
            print("Win")
            print("Congratulations! Can you give me high score?")
    else:
        print("Enter again!")

import sys
import msvcrt
print("Press any key to close")
msvcrt.getch()
sys.exit()
















