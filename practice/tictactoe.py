board = [" " for _ in range(9)]


def display_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(player):
    combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    return any(
        board[a] == board[b] == board[c] == player
        for a, b, c in combinations
    )


def board_full():
    return " " not in board


player = "X"

while True:
    display_board()

    try:
        position = int(input(f"Player {player}, choose position (1-9): ")) - 1

        if position < 0 or position > 8:
            print("Choose a position from 1 to 9.")
            continue

        if board[position] != " ":
            print("That position is already occupied.")
            continue

        board[position] = player

        if check_winner(player):
            display_board()
            print(f"Player {player} wins!")
            break

        if board_full():
            display_board()
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"

    except ValueError:
        print("Please enter a valid number.")