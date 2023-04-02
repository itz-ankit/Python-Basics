import random

# Function to display the Tic Tac Toe board
def display_board(board):
    print("   |   |")
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("---|---|---")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("---|---|---")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])
    print("   |   |")

# Function to check if a player has won the game
def check_win(board, mark):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == mark:
            return True
    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == mark:
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    return False

# Function to get the user's move
def get_player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            row = (move-1) // 3
            col = (move-1) % 3
            if board[row][col] != " ":
                print("That spot is already taken!")
            else:
                return (row, col)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# Function to get the bot's move
def get_bot_move(board, mark):
    # Check if there is a winning move for the bot
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = mark
                if check_win(board, mark):
                    return (i, j)
                else:
                    board[i][j] = " "
    # Check if there is a winning move for the player
    if mark == "X":
        player_mark = "O"
    else:
        player_mark = "X"
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = player_mark
                if check_win(board, player_mark):
                    board[i][j] = mark
                    return (i, j)
                else:
                    board[i][j] = " "
    # Choose a random spot
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            return (row, col)

# Function to play the game
def play_game():
    board = [[" " for i in range(3)] for j in range(3)]
    print("Let's play Tic Tac Toe!")
    print("You are X and the bot is O.")
    display_board(board)
    turn = "player"
    while True:
        # Player's turn
        if turn == "player":
            display_board(board)
            row, col = get_player_move(board)
            board[row][col] = "X"
            if check_win(board, "X"):
                display_board(board)
                print("Congratulations! You win!")
                return
            if " " not in [spot for row in board for spot in row]:
                display_board(board)
                print("It's a tie!")
                return
            turn = "bot"
        # Bot's turn
        else:
            print("The bot is making a move...")
            row, col = get_bot_move(board, "O")
            board[row][col] = "O"
            if check_win(board, "O"):
                display_board(board)
                print("The bot wins! Better luck next time.")
                return
            if " " not in [spot for row in board for spot in row]:
                display_board(board)
                print("It's a tie!")
                return
            turn = "player"

#play the game
play_game()