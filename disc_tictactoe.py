import discord
import random
import asyncio

client = discord.Client()

# Define constants for game states
EMPTY = "-"
X = "X"
O = "O"

# Define the Tic Tac Toe board
board = [EMPTY] * 9

# Define a list of winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]               # Diagonals
]

# Define helper functions

def is_winner(board, player):
    """
    Check if a player has won the game.
    """
    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False

def is_draw(board):
    """
    Check if the game is a draw.
    """
    return EMPTY not in board

def get_free_positions(board):
    """
    Get a list of indices of free positions on the board.
    """
    return [i for i in range(9) if board[i] == EMPTY]

def make_move(board, position, player):
    """
    Make a move on the board.
    """
    board[position] = player

def get_bot_move(board, bot_player):
    """
    Get the bot's move.
    """
    free_positions = get_free_positions(board)
    return random.choice(free_positions)

async def start_game(message):
    """
    Start a new Tic Tac Toe game.
    """
    global board
    board = [EMPTY] * 9
    current_player = X
    game_over = False

    # Send an initial message with the empty board
    await message.channel.send('Let\'s play Tic Tac Toe!\n' + get_board_string(board))

    # Main game loop
    while not game_over:
        if current_player == O:
            # Bot's turn
            bot_move = get_bot_move(board, O)
            make_move(board, bot_move, O)
            await message.channel.send(get_board_string(board))
            if is_winner(board, O):
                await message.channel.send('Bot wins!')
                game_over = True
            elif is_draw(board):
                await message.channel.send('It\'s a draw!')
                game_over = True
            else:
                current_player = X
        else:
            # User's turn
            def check_move(m):
                return m.author == message.author and m.channel == message.channel

            try:
                user_move_message = await client.wait_for('message', timeout=60.0, check=check_move)
                user_move = int(user_move_message.content)
                if user_move < 1 or user_move > 9 or board[user_move - 1] != EMPTY:
                    await message.channel.send('Invalid move. Please choose an empty position (1-9):')
                else:
                    make_move(board, user_move - 1, X)
                    await message.channel.send(get_board_string(board))
                    if is_winner(board, X):
                        await message.channel.send('You win!')
                        game_over = True
                    elif is_draw(board):
                        await message.channel.send('It\'s a draw!')
                        game_over = True
                    else:
                        current_player = O
            except asyncio.TimeoutError:
                await message.channel.send('Game timed out. Exiting...')
                game_over = True 
def get_board_string(board):
    """
    Get a string representation of the board.
    """
    board_string = ""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            board_string += "|\n"
        board_string += board[i] + " "
    board_string += "|\n"
    return board_string

@client.event
async def on_ready():
    """
    Event handler for when the bot is ready.
    """
    print(f'Logged in as {client.user.name}')
    print('------')

@client.event
async def on_message(message):
    """
    Event handler for incoming messages.
    """
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    if message.content == 'start game':
        await start_game(message)

# Replace 'YOUR_TOKEN_HERE' with your Discord bot token
client.run('YOUR_TOKEN_HERE')

