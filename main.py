import os

def main():
    print("Welcome to Tic Tac Toe game!!!")
    player1_score = 0
    player2_score = 0
    board, current_player = reset_game()

    while True:
        clear_console()
        print(f"Score: X {player1_score} : O {player2_score}")
        print_board(board)

        row, col = get_player_move(board)
        update_board(board, row, col, current_player)

        if check_winner(board, current_player):
            print(f"Player {current_player.upper()} wins the game!")
            print_board(board)

            if current_player == "x":
                player1_score += 1
            else:
                player2_score += 1

            if not play_again():
                print(f"Final Score: X {player1_score} : O {player2_score}")
                break
            board, current_player = reset_game()
        elif is_draw(board):
            print("It's a draw!")
            print_board(board)

            if not play_again():
                break
            board, current_player = reset_game()
        else:
            current_player = switch_player(current_player)


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_board(board):
    """Prints the current state of the board."""
    print("+" + "---+" * len(board[0]))

    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+" + "---+" * len(board[0]))


def get_player_move(board):
    """Prompts the user to enter a valid move."""
    while True:
        try:
            row = int(input("Input row (1-3): ")) - 1
            col = int(input("Input column (1-3): ")) - 1

            if not (0 <= row < 3 and 0 <= col < 3):
                print("Input out of range. Try again.")
            elif board[row][col] != " ":
                print("This field is already taken. Choose another one.")
            else:
                return row, col
        except ValueError:
            print("Invalid input. Please enter numbers only.")


def update_board(board, row, col, player):
    """Updates the board with the player's move."""
    board[row][col] = player


def check_winner(board, player):
    """Checks if the given player has won the game."""
    return (
        any(all(cell == player for cell in row) for row in board) or  # Horizontal
        any(all(row[i] == player for row in board) for i in range(3)) or  # Vertical
        all(board[i][i] == player for i in range(3)) or  # Main diagonal
        all(board[i][2 - i] == player for i in range(3))  # Anti-diagonal
    )


def is_draw(board):
    """Checks if the game is a draw (no empty cells left)."""
    return all(cell != " " for row in board for cell in row)


def switch_player(player):
    """Switches the current player."""
    return "o" if player == "x" else "x"


def play_again():
    """Asks the players if they want to play again."""
    while True:
        try:
            choice = int(input("Play again? (1 for Yes, 2 for No): "))
            if choice == 1:
                return True
            elif choice == 2:
                return False
            else:
                print("Invalid choice. Enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")


def reset_game():
    """Resets the board and returns it along with the first player."""
    return [[" " for _ in range(3)] for _ in range(3)], "x"


if __name__ == "__main__":
    main()
