import random

# Define the game constants
WIDTH = 10
HEIGHT = 10
DRAGON = "D"
TREASURE = "T"
OBSTACLE = "X"
EMPTY = " "
WINNING_SCORE = 5

# Initialize the game state
game_map = [[EMPTY for _ in range(WIDTH)] for _ in range(HEIGHT)]
dragon_x = random.randint(0, WIDTH - 1)
dragon_y = random.randint(0, HEIGHT - 1)
treasure_x = random.randint(0, WIDTH - 1)
treasure_y = random.randint(0, HEIGHT - 1)
obstacle_x = random.randint(0, WIDTH - 1)
obstacle_y = random.randint(0, HEIGHT - 1)
score = 0

# Main game loop
while True:
    # Draw the game map
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if x == dragon_x and y == dragon_y:
                print(DRAGON, end=" ")
            elif x == treasure_x and y == treasure_y:
                print(TREASURE, end=" ")
            elif x == obstacle_x and y == obstacle_y:
                print(OBSTACLE, end=" ")
            else:
                print(EMPTY, end=" ")
        print()
    print("Score:", score)

    # Get player input
    move = input("Enter your move (w/a/s/d): ")

    # Update game state based on player input
    if move == "w" and dragon_y > 0:
        dragon_y -= 1
    elif move == "a" and dragon_x > 0:
        dragon_x -= 1
    elif move == "s" and dragon_y < HEIGHT - 1:
        dragon_y += 1
    elif move == "d" and dragon_x < WIDTH - 1:
        dragon_x += 1

    # Check for collision with treasure
    if dragon_x == treasure_x and dragon_y == treasure_y:
        print("You found treasure!")
        score += 1
        treasure_x = random.randint(0, WIDTH - 1)
        treasure_y = random.randint(0, HEIGHT - 1)

    # Check for collision with obstacle
    if dragon_x == obstacle_x and dragon_y == obstacle_y:
        print("You ran into an obstacle!")
        score -= 1
        obstacle_x = random.randint(0, WIDTH - 1)
        obstacle_y = random.randint(0, HEIGHT - 1)

    # Check for winning condition
    if score >= WINNING_SCORE:
        print("Congratulations, you won!")
        break
