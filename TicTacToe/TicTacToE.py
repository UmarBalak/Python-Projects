import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

# Printing the game board
def printBoard(board):
    print("╔═══╦═══╦═══╗")
    print("║ " + board[0] + " ║ " + board[1] + " ║ " + board[2] + " ║ ")
    print("╠═══╬═══╬═══╣")
    print("║ " + board[3] + " ║ " + board[4] + " ║ " + board[5] + " ║ ")
    print("╠═══╬═══╬═══╣")
    print("║ " + board[6] + " ║ " + board[7] + " ║ " + board[8] + " ║ ")
    print("╚═══╩═══╩═══╝")

# Function to check the win condition
def checkWin(board, player):
    # Rows
    if board[0] == board[1] == board[2] == player:
        return True
    if board[3] == board[4] == board[5] == player:
        return True
    if board[6] == board[7] == board[8] == player:
        return True
    # Columns
    if board[0] == board[3] == board[6] == player:
        return True
    if board[1] == board[4] == board[7] == player:
        return True
    if board[2] == board[5] == board[8] == player:
        return True
    # Diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to check if the board is full
def isBoardFull(board):
    return "-" not in board

# Function to switch players
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# Function for the computer's move
def computerMove():
    availablePositions = [i for i in range(len(board)) if board[i] == "-"]
    randomPosition = random.choice(availablePositions)
    board[randomPosition] = currentPlayer

# Function for playing with a computer
def playWithComputer():
    global currentPlayer, winner, gameRunning
    while gameRunning:
        printBoard(board)
        if currentPlayer == "X":
            inp = int(input("Enter the position (1-9): "))
            if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
                board[inp - 1] = currentPlayer
                if checkWin(board, currentPlayer):
                    winner = currentPlayer
                    gameRunning = False
                elif isBoardFull(board):
                    gameRunning = False
                else:
                    switchPlayer()
            else:
                print("Oops! The spot is occupied or the input is invalid.")
        else:
            computerMove()
            if checkWin(board, currentPlayer):
                winner = currentPlayer
                gameRunning = False
            elif isBoardFull(board):
                gameRunning = False
            else:
                switchPlayer()

# Function for playing with a friend
def playWithFriend():
    global currentPlayer, winner, gameRunning
    while gameRunning:
        printBoard(board)
        inp = int(input("Enter the position (1-9): "))
        if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
            board[inp - 1] = currentPlayer
            if checkWin(board, currentPlayer):
                winner = currentPlayer
                gameRunning = False
            elif isBoardFull(board):
                gameRunning = False
            else:
                switchPlayer()
        else:
            print("Oops! The spot is occupied or the input is invalid.")

# Main game loop
while True:
    mode = input("Choose game mode (1 - Play with computer, 2 - Play with a friend): ")
    if mode == "1":
        playWithComputer()
        break
    elif mode == "2":
        playWithFriend()
        break
    else:
        print("Invalid input. Please choose 1 or 2.")

printBoard(board)

if winner:
    print("✨ Congratulations! Player", winner, "wins! ✨")
else:
    print("It's a tie! 🤝")
