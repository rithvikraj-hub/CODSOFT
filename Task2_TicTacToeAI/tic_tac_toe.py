import math
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_winner(board):
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    for row in board:
        if " " in row:
            return None

    return "Draw"
def minimax(board, depth, is_maximizing):
    result = check_winner(board)

    if result == "O":
        return 1
    elif result == "X":
        return -1
    elif result == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)

        return best_score
def ai_move(board):
    best_score = -math.inf
    move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "

                if score > best_score:
                    best_score = score
                    move = (i, j)

    board[move[0]][move[1]] = "O"
def human_move(board):
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))

            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Cell already occupied!")

        except:
            print("Invalid input! Try again.")
board = [[" " for _ in range(3)] for _ in range(3)]

print("Welcome to Tic-Tac-Toe!")
print("You are X, AI is O")

while True:
    print_board(board)

    human_move(board)

    result = check_winner(board)
    if result:
        print_board(board)
        print("Result:", result)
        break

    ai_move(board)

    result = check_winner(board)
    if result:
        print_board(board)
        print("Result:", result)
        break
