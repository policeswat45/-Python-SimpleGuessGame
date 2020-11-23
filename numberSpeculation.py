"""
Author:           Antares
Date:             Nov 23rd 2020
Name of the game: Guessing Number

How to play:
-Press 1 to Start/2 to End
-Type in the number from 1 to 11
-If your number is equal to machine, you won; otherwise, machine won!

Please enjoy! (probably only me lmao)
"""
import random
from time import sleep      #for sleep function
import os

def main_game ():
    option = int(input("Type 1 to play or 2 to end "))
    while True:
        while option > 2:
            print("Unable to comply! Please select the right option!")
            option = int(input("Type 1 to play or 2 to end "))

            if option <= 2:
                break

        if option == 2:
            break

        playerNumber = int (input ("What is your verdict? (From 1 to 11) "))
        while playerNumber < 1 or playerNumber > 11:
            print ("Please only select the number from 1 to 11")
            playerNumber = int (input("What is your verdict? (From 1 to 11) "))

        machineNumber = random.randint(1,11)
        print ("The number of Machine is ",  machineNumber)
        print("The number of Player is ",  playerNumber)

        if playerNumber ==  machineNumber:

           print ("You won!")

        else:

            print ("The machine won!")

        input("Press Enter to continue...")
        #sleep(1)         #You can add sleep function here to slow it down
        os.system('cls')  #Clear screen function; you need to turn on "Emulate terminal" in Run/Edit Config

main_game()
