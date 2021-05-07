import random

print("Rock, Paper, Scissors")
userChoice = input("Input the following R,P,S.\n")
robotVal = random.randint(1,3)
if (robotVal == 1):
    robotChoice = 'R'
    robotStr = 'Rock'
elif (robotVal == 2):
    robotChoice = 'P'
    robotStr = 'Paper'
elif (robotVal == 3):
    robotChoice = 'S'
    robotStr = 'Scissors'

if(userChoice == robotChoice):
    print(f"TIE. You have both chosen {robotStr}.")
elif (userChoice == 'R'): #User chose Rock
    if(robotChoice == 'P'): #Robot chose Paper
        print(f"YOU LOSE. The Robot chose {robotStr}.")
    elif(robotChoice == 'S'): #Robot chose Scissors
        print(f"YOU WIN. The Robot chose {robotStr}.")

elif (userChoice == 'P'): #User chose Paper
    if(robotChoice == 'R'): #Robot chose Rock
        print(f"YOU WIN. The Robot chose {robotStr}.")
    elif(robotChoice == 'S'): #Robot chose Scissors
        print(f"YOU LOSE. The Robot chose {robotStr}.")

elif (userChoice == 'S'): #User chose Paper
    if(robotChoice == 'R'): #Robot chose Rock
        print(f"YOU LOSE. The Robot chose {robotStr}.")
    elif(robotChoice == 'P'): #Robot chose Paper
        print(f"YOU WIN. You have both chosen {robotStr}.")