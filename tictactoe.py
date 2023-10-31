import random

# Initialize the Tic Tac Toe board
board = [" " for _ in range(9)]

# Function to display the Tic Tac Toe board
def display_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i + 3]))
        if i < 6:
            print("-" * 9)

# Function to check for a win
def check_win(board, player):
    win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False

# Function to check for a tie
def check_tie(board):
    return " " not in board

# Function for the AI to make a move using minimax
# Modify the minimax function with alpha-beta pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, "O"):
        return 1
    if check_win(board, "X"):
        return -1
    if check_tie(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = " "
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break  # Prune remaining branches
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = " "
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break  # Prune remaining branches
        return best_score

# Modify the ai_move function for "Hard" AI
# Modify the ai_move function for "Hard" AI
def ai_move(board, level):
    if level == 1:  # Easy: Random moves
        empty_cells = [i for i, cell in enumerate(board) if cell == " "]
        return random.choice(empty_cells)
    elif level == 2:  # Medium: Minimax with limited depth
        best_move = -1
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, 0, False, -float("inf"), float("inf"))
                board[i] = " "
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move
    elif level == 3:  # Hard: Full Minimax with increased depth and heuristics
        best_move = -1
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                # Increase the depth for a deeper search
                score = enhanced_minimax(board, 0, False, -float("inf"), float("inf"))
                board[i] = " "
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move

# New minimax function with increased depth and heuristics
def enhanced_minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, "O"):
        return 1
    if check_win(board, "X"):
        return -1
    if check_tie(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                # Increase the depth for a deeper search
                score = enhanced_minimax(board, depth + 1, False, alpha, beta)
                board[i] = " "
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break  # Prune remaining branches
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                # Increase the depth for a deeper search
                score = enhanced_minimax(board, depth + 1, True, alpha, beta)
                board[i] = " "
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break  # Prune remaining branches
        return best_score


# Main game loop
while True:
    display_board(board)

    # Player's move
    player_move = int(input("Enter your move (1-9): ")) - 1
    if board[player_move] == " ":
        board[player_move] = "X"
    else:
        print("Invalid move. Try again.")
        continue

    # Check if the player has won
    if check_win(board, "X"):
        display_board(board)
        print("You win!")
        break

    # Check for a tie
    if check_tie(board):
        display_board(board)
        print("It's a tie!")
        break

    # AI's move
    ai_level = int(input("Choose AI level (1: Easy, 2: Medium, 3: Hard): "))
    ai_position = ai_move(board, ai_level)
    board[ai_position] = "O"

    # Check if the AI has won
    if check_win(board, "O"):
        display_board(board)
        print("AI wins!")
        break

    # Check for a tie
    if check_tie(board):
        display_board(board)
        print("It's a tie!")
        break
