import random

print("Hello, what's your name?")
username = input()

userGuess = int(input(f"Okay {username}, I am guessing a number from 1 to 10. Can you guess it?\n"))
robotNumber = random.randint(1,10)
i = 1
while(userGuess != robotNumber):
    if(userGuess < robotNumber):
        print("Your guess is too low")
    elif(userGuess > robotNumber):
        print("Your guess is too high")
    i += 1
    userGuess = int(input())
print(f"You guessed it in {i} tries!")
