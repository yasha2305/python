
import random

players = ["Player 1", "Player 2", "Player 3", "Player 4"]
tokens = {player: [0, 0, 0, 0] for player in players}

# 0 = token at home, 1-56 = token progress, 57 = finished
FINISH = 57

print("=" * 40)
print("          🎲 LUDO GAME 🎲")
print("=" * 40)

num_players = int(input("Enter number of players (2-4): "))

if num_players < 2 or num_players > 4:
    print("Please choose between 2 and 4 players.")
    raise SystemExit

players = players[:num_players]
tokens = {player: [0, 0, 0, 0] for player in players}

while True:
    for player in players:
        print(f"\n{player}'s turn")
        input("Press Enter to roll the dice...")

        dice = random.randint(1, 6)
        print(f"🎲 You rolled: {dice}")

        print("Your tokens:")
        for i, position in enumerate(tokens[player], start=1):
            if position == 0:
                status = "HOME"
            elif position == FINISH:
                status = "FINISHED"
            else:
                status = f"Position {position}"
            print(f"  Token {i}: {status}")

        available = [
            i for i, pos in enumerate(tokens[player])
            if pos < FINISH and (pos > 0 or dice == 6)
        ]

        if not available:
            print("No token can move! You need a 6 to leave home.")
            continue

        while True:
            try:
                choice = int(input("Choose token (1-4): ")) - 1
                if choice in available:
                    break
                print("That token cannot move. Choose an available token.")
            except ValueError:
                print("Enter a valid number.")

        position = tokens[player][choice]

        if position == 0 and dice == 6:
            tokens[player][choice] = 1
            print(f"{player} brought Token {choice + 1} out of home!")
        elif position > 0 and position + dice <= FINISH:
            tokens[player][choice] += dice
            print(
                f"Token {choice + 1} moved to "
                f"position {tokens[player][choice]}!"
            )
        else:
            print("That move would exceed the finish. No movement.")

        if all(pos == FINISH for pos in tokens[player]):
            print(f"\n🏆 {player} WINS THE LUDO GAME! 🏆")
            break

    else:
        continue

    break