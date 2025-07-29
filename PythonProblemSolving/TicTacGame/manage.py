# Function to print the board
def print_board(board):
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

# Function to check for winner
def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8],   # columns
        [0,4,8], [2,4,6]             # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Main game logic
def play_game():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    current_player = "X"
    moves = 0

    while True:
        print_board(board)
        move = input(f"Player {current_player}, choose a position (1-9): ")

        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("❌ Invalid input. Try again.")
            continue

        move = int(move) - 1

        if board[move] in ["X", "O"]:
            print("❌ That spot is already taken. Choose another.")
            continue

        board[move] = current_player
        moves += 1

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        if moves == 9:
            print_board(board)
            print("🤝 It's a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
play_game()
