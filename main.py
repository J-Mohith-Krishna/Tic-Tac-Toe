def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return True, row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True, board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True, board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True, board[0][2]
    return False, None

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (1-3): ")) - 1
        col = int(input(f"Player {current_player}, enter column (1-3): ")) - 1
        if board[row][col] == ' ':
            board[row][col] = current_player
            winner_found, winner = check_winner(board)
            if winner_found:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            if all(all(cell != ' ' for cell in row) for row in board):
                print_board(board)
                print("It's a tie!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That position is already taken. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
