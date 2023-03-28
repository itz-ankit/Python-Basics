def print_board(board):
    """Prints the current state of the board"""
    print("   |   |   ")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("   |   |   ")

def get_move(board, player):
    """Asks the player for their move and returns the updated board"""
    while True:
        try:
            move = int(input(f"{player}, enter a number from 1 to 9: "))
            if move < 1 or move > 9:
                print("Invalid move. Please enter a number from 1 to 9.")
            elif board[move - 1] != " ":
                print("That spot is already taken. Please choose another spot.")
            else:
                board[move - 1] = player
                return board
        except ValueError:
            print("Invalid move. Please enter a number from 1 to 9.")

def check_winner(board):
    """Checks if there is a winner"""
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != " ":
            return board[i]
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != " ":
            return board[i]
    # Check diagonals
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    # Check if the board is full (tie)
    if " " not in board:
        return "Tie"
    # No winner yet
    return None

def play_game():
    """Plays the Tic Tac Toe game"""
    print("Welcome to Tic Tac Toe!")
    print("Player 1: X")
    print("Player 2: O")
    board = [" "] * 9
    player = "X"
    while True:
        print_board(board)
        board = get_move(board, player)
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == "Tie":
                print("It's a tie!")
            else:
                print(f"{winner} wins!")
            break
        # Switch players
        player = "O" if player == "X" else "X"

# Start the game
play_game()