def main():
    wordGuess = input("Player 1: Type in a word: ")
    wordlen = len(wordGuess)
    Guesses = 0
    arr = ['_'] * wordlen
    print("Player 2: Guess any letter")
    while Guesses <= 6:
        letter = input()
        for i in range(wordlen):
           if letter == wordGuess[i]:
               arr[i] = letter
    print(arr)
if __name__ == '__main__':
    main()