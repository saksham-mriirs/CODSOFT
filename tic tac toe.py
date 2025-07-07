import math

# Initialize board
board = [' ' for _ in range(9)]

# Print the board
def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")

# Check for a win
def check_winner(player):
    win_cond = [
        [0,1,2], [3,4,5], [6,7,8], # Rows
        [0,3,6], [1,4,7], [2,5,8], # Columns
        [0,4,8], [2,4,6]           # Diagonals
    ]
    for combo in win_cond:
        if all(board[i] == player for i in combo):
            return True
    return False

# Check if board is full
def is_draw():
    return ' ' not in board

# Minimax algorithm
def minimax(is_maximizing):
    if check_winner('O'):
        return 1
    elif check_winner('X'):
        return -1
    elif is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# AI move
def ai_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

# Human move
def human_move():
    while True:
        try:
            pos = int(input("Enter your move (1-9): ")) - 1
            if board[pos] == ' ':
                board[pos] = 'X'
                break
            else:
                print("That position is already taken.")
        except (IndexError, ValueError):
            print("Invalid input. Choose a number between 1 and 9.")

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe! You are 'X'. AI is 'O'.")
    print_board()

    while True:
        human_move()
        print_board()
        if check_winner('X'):
            print("You win!")
            break
        if is_draw():
            print("It's a draw!")
            break

        ai_move()
        print("AI played:")
        print_board()
        if check_winner('O'):
            print("AI wins!")
            break
        if is_draw():
            print("It's a draw!")
            break

# Run the game
play_game()
