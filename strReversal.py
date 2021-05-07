def main():
    revStr = [] #make an array to store the reverse string
    userInput = input("Please enter a sentence to reverse.\n")
    index = len(userInput)
    while index > 0: #as long as the length of the input is greater than 0
        revStr += userInput[index-1] #we add each letter into the array, but from last index (reverse order)
        index-= 1 #decrement
    result = ''.join(revStr) #we join it together. (array to str)
    print(result)

if __name__ == '__main__':
    main()