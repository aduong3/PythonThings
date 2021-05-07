def main():
    amt = []
    print("Let's calculate some numbers!")
    amount = int(input("How many numbers are we calculating? "))
    print("Please input the numbers now: ")
    for i in range(amount):
        number = int(input())
        amt.append(number)
    operation = input("Select one of the following operation: +,-,/,*\n")
    if(operation == '+'):
        #result = sum(amt)
        result = 0
        for i in range(amount):
            result += amt[i]
    elif(operation == '-'):
        result = amt[0]
        for i in range(1,amount):
            result -= amt[i]
    elif(operation == '/'):
        result = amt[0]
        for i in range(1,amount):
            result = result/amt[i]
    elif(operation == '*'):
        result = 1
        for i in range(amount):
            result = result*amt[i]
    print(f'The final result is {result}')
if __name__ == '__main__':
    main()