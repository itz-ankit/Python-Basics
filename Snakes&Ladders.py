import os
import random

# Define the game board
board = {
    1: 38, 4: 14, 8: 30, 21: 42, 28: 76, 50: 67, 71: 92, 80: 99,
    32: 10, 36: 6, 48: 26, 62: 18, 88: 24, 95: 56, 97: 78
}

# Define the players
players = {
    "Player 1": 0,
    "Player 2": 0
}

# Define the visual board
def print_board():
    print("+" + "-"*39 + "+")
    for row in range(10, 0, -1):
        line = "|"
        for col in range(1, 11):
            square = row * 10 - col + 1
            if square in board:
                line += f"{board[square]:2d}|"
            elif players["Player 1"] == square:
                line += "P1|"
            elif players["Player 2"] == square:
                line += "P2|"
            else:
                line += "  |"
        print(line)
        print("+" + "-"*39 + "+")

# Define the game logic
def play():
    turn = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') # Clear the console screen
        print_board()
        for player in players:
            input(f"{player}, press Enter to roll the dice...")
            dice = random.randint(1, 6)
            print(f"{player} rolled {dice}.")
            players[player] += dice
            if players[player] in board:
                if players[player] < board[players[player]]:
                    print(f"Oops, {player} landed on a snake! Moving back to {board[players[player]]}.")
                else:
                    print(f"Wow, {player} landed on a ladder! Moving up to {board[players[player]]}.")
                players[player] = board[players[player]]
            if players[player] >= 100:
                os.system('cls' if os.name == 'nt' else 'clear') # Clear the console screen
                print_board()
                print(f"Congratulations, {player} won!")
                return
            os.system('cls' if os.name == 'nt' else 'clear') # Clear the console screen
            print_board()
            print(f"{player} is now on square {players[player]}.")
        turn += 1
        print(f"End of turn {turn}.")

# Start the game
play()
