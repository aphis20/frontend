import random

def print_board(board):
    print("  0 1 2")
    for row in range(3):
        print(row, ' '.join(board[row]))

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
       (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True
    return False

def check_draw(board):
    return all([cell != ' ' for row in board for cell in row])

def player_move(board):
    while True:
        try:
            row, col = map(int, input("Enter your move (row and column): ").split())
            if board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("The cell is already taken! Try again.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter row and column numbers between 0 and 2.")

def computer_move(board):
    # Try to find a move to win or block the opponent
    for player in ['O', 'X']:
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = player
                    if check_win(board, player):
                        if player == 'O':
                            return  # Computer plays this move
                        board[i][j] = 'O'  # Block the player and continue
                        return
                    board[i][j] = ' '  # Reset the move if not winning/blocking
    
    # Random move as fallback
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    move = random.choice(empty_cells)
    board[move[0]][move[1]] = 'O'

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print_board(board)
    
    while True:
        # Player's move
        player_move(board)
        print_board(board)
        if check_win(board, 'X'):
            print("Congratulations! You win!")
            return 'Player'
        if check_draw(board):
            print("It's a draw!")
            return 'Draw'

        # Computer's move
        computer_move(board)
        print_board(board)
        if check_win(board, 'O'):
            print("Computer wins! Better luck next time.")
            return 'Computer'
        if check_draw(board):
            print("It's a draw!")
            return 'Draw'

def main():
    print("Welcome to Tic-Tac-Toe!")
    scores = {'Player': 0, 'Computer': 0, 'Draw': 0}
    
    while True:
        result = play_game()
        scores[result] += 1
        print(f"Scores: Player {scores['Player']} - Computer {scores['Computer']} - Draw {scores['Draw']}")
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
