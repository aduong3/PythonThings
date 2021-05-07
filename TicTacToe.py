import random
import time
def printBoard(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    return board

def BotTurn(board,playerIcon,botIcon):
    botTime = -1
    botCounter = 0
    while(botTime == -1):
        botChoice = random.randint(0,8)
        if(board[botChoice] == botChoice):
            board[botChoice] = botIcon
            botTime = 1
        elif(board[botChoice] == botIcon or board[botChoice] == playerIcon):
            botCounter+=1
            if(botCounter == 10):
                break
            else:
                continue

def YourTurn(board,playerIcon,botIcon):
    playerTime = -1
    while(playerTime == -1):
        playerChoice = int(input("YOUR TURN. SELECT A NUMBER: "))
        if(board[playerChoice] == playerChoice):
            board[playerChoice] = playerIcon
            playerTime = 1
        elif(board[playerChoice] == botIcon or board[playerChoice] == playerIcon):
            print("Please play a valid move.")
            continue

def main():
    board = [0,1,2,3,4,5,6,7,8]
    winner = -1
    TurnCounter = 0
    print("Hello and welcome to Tic-Tac-Toe!")
    playerIcon = input("X or O: ")
    if playerIcon == 'X':
        botIcon = 'O'
    elif playerIcon == 'O':
        botIcon = 'X'

    for i in range(10):
            printBoard(board)
            YourTurn(board,playerIcon,botIcon)
            TurnCounter+=1
            if(TurnCounter >= 5):
                if(board[0] == board[1] == board[2]): #top row
                    if(board[0] == playerIcon):
                        print("WINNER")
                        winner = 1
                        print("FINAL BOARD")
                        printBoard(board)
                        break
                    if(board[0] == botIcon):
                        print("LOSER")
                        winner = 1
                        print("FINAL BOARD")
                        printBoard(board)
                        break
                elif(board[3] == board[4] == board[5]): #middle row
                    if(board[3] == playerIcon):
                        print("WINNER")
                        winner = 1
                        print("FINAL BOARD")
                        printBoard(board)
                        break
                    if(board[3] == botIcon):
                        print("LOSER")
                        winner = 1
                        print("FINAL BOARD")
                        printBoard(board)
                        break
                elif(board[6] == board[7] == board[8]): #bottom row
                    if(board[6] == playerIcon):
                        print("WINNER")
                        winner = 1
                        print("FINAL BOARD")
                        printBoard(board)
                        break
                    if(board[6] == botIcon):
                        print("LOSER")
                        winner = 1
                        print("FINAL BOARD")
                        printBoard(board)
                        break
                elif(board[0] == board[3] == board[6]): #1st column
                    if(board[0] == playerIcon):
                        print("WINNER")
                        winner = 1
                        print("FINAL BOARD")
                        printBoard(board)
                        break
                    if(board[0] == botIcon):
                        print("LOSER")
                        winner = 1
                        print("FINAL BOARD")
                        printBoard(board)
                        break   
                elif(board[1] == board[4] == board[7]): #2nd row
                    if(board[1] == playerIcon):
                        print("WINNER")
                        winner = 1
                        print("FINAL BOARD")
                        printBoard(board)
                        break
                    if(board[1] == botIcon):
                        print("LOSER")
                        winner = 1
                        print("FINAL BOARD")
                        printBoard(board)
                        break
                elif(board[2] == board[5] == board[8]): #3rd row
                    if(board[2] == playerIcon):
                        print("WINNER")
                        winner = 1
                        print("FINAL BOARD")
                        printBoard(board)
                        break
                    if(board[2] == botIcon):
                        print("LOSER")
                        winner = 1
                        print("FINAL BOARD")
                        printBoard(board)
                        break
                elif(board[0] == board[4] == board[8]): #diagonal row
                    if(board[0] == playerIcon):
                        print("WINNER")
                        winner = 1
                        print("FINAL BOARD")
                        printBoard(board)
                        break
                    if(board[0] == botIcon):
                        print("LOSER")
                        winner = 1
                        print("FINAL BOARD")
                        printBoard(board)
                        break
                elif(board[2] == board[4] == board[6]): #2nd diagonal row
                    if(board[2] == playerIcon):
                        print("WINNER")
                        winner = 1
                        print("FINAL BOARD")
                        printBoard(board)
                        break
                    if(board[2] == botIcon):
                        print("LOSER")
                        winner = 1
                        print("FINAL BOARD")
                        printBoard(board)
                        break
                elif(board[0] != 0 and board[1] != 1 and board[2] != 2 and board[3] != 3 and board[4] != 4 and board[5] != 5 and board[6] != 6 and board[7] != 7 and board[8] != 8):
                    print("TIE GAME")
                    winner = 1
                    print("FINAL BOARD")
                    printBoard(board)
                    break
            if(winner != 1):
                BotTurn(board,playerIcon,botIcon)
                TurnCounter+=1


if __name__ == '__main__':
    main()