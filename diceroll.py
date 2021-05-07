import random
# we want to roll between 1 and 6
saveRolls = []
numOfDie = int(input("How many die would you like to roll? ")) #must specify int for input so for loop can work
for i in range(numOfDie): #range needs an int value
    roll = random.randint(1,6) 
    print(f'Dice {i + 1} : {roll}')
    saveRolls.append(roll)

print(f"The sum of your rolls is {sum(saveRolls)}")