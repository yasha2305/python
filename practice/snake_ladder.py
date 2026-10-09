import random

# Snakes: head -> tail
snakes = {
    99: 54,
    95: 72,
    92: 51,
    87: 36,
    62: 19,
    64: 60,
    47: 26,
    49: 11,
    16: 6
}

# Ladders: bottom -> top
ladders = {
    2: 38,
    7: 14,
    8: 31,
    15: 26,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91
}

player1 = 0
player2 = 0


def roll_dice():
    return random.randint(1, 6)


def move_player(position, dice):
    new_position = position + dice

    # Player cannot go beyond 100
    if new_position > 100:
        return position

    # Check ladder
    if new_position in ladders:
        print(f"🪜 Ladder! {new_position} -> {ladders[new_position]}")
        new_position = ladders[new_position]

    # Check snake
    elif new_position in snakes:
        print(f"🐍 Snake! {new_position} -> {snakes[new_position]}")
        new_position = snakes[new_position]

    return new_position


print("=" * 40)
print("        🐍 SNAKE & LADDER 🪜")
print("=" * 40)
print("Player 1 vs Player 2")
print("First player to reach 100 wins!")
print()

while True:

    # Player 1 turn
    input("Player 1 - Press Enter to roll the dice...")

    dice = roll_dice()
    print(f"🎲 Player 1 rolled: {dice}")

    player1 = move_player(player1, dice)

    print(f"📍 Player 1 position: {player1}")
    print(f"📍 Player 2 position: {player2}")
    print()

    if player1 == 100:
        print("🎉 Player 1 WINS!")
        break

    # Player 2 turn
    input("Player 2 - Press Enter to roll the dice...")

    dice = roll_dice()
    print(f"🎲 Player 2 rolled: {dice}")

    player2 = move_player(player2, dice)

    print(f"📍 Player 1 position: {player1}")
    print(f"📍 Player 2 position: {player2}")
    print()

    if player2 == 100:
        print("🎉 Player 2 WINS!")
        break

print()
print("=" * 40)
print("          GAME OVER")
print("=" * 40) 
