import random

class Player:
    def __init__(self):
        self.health = 100
        self.gold = 0
        self.level = 1

    def show_stats(self):
        print("\n===== PLAYER STATS =====")
        print(f"Health: {self.health}")
        print(f"Gold: {self.gold}")
        print(f"Level: {self.level}")

player = Player()

monsters = [
    {"name": "Goblin", "health": 30, "attack": 10},
    {"name": "Skeleton", "health": 40, "attack": 12},
    {"name": "Orc", "health": 50, "attack": 15},
    {"name": "Dragon", "health": 80, "attack": 20}
]

def battle(player, monster):

    print(f"\n⚔️ A {monster['name']} appears!")

    monster_hp = monster["health"]

    while monster_hp > 0 and player.health > 0:

        print(
            f"\nYour HP: {player.health}"
        )
        print(
            f"{monster['name']} HP: {monster_hp}"
        )

        action = input(
            "Attack (a) or Run (r): "
        ).lower()

        if action == "r":

            if random.randint(1, 100) <= 50:
                print("🏃 You escaped!")
                return
            else:
                print("❌ Escape failed!")

        damage = random.randint(8, 20)
        monster_hp -= damage

        print(
            f"You dealt {damage} damage!"
        )

        if monster_hp <= 0:
            reward = random.randint(10, 50)

            player.gold += reward

            player.level += 1

            print(
                f"🎉 Monster defeated!"
            )

            print(
                f"💰 Found {reward} gold!"
            )

            return

        monster_damage = random.randint(
            1,
            monster["attack"]
        )

        player.health -= monster_damage

        print(
            f"{monster['name']} hit you for "
            f"{monster_damage} damage!"
        )

def explore():

    event = random.choice([
        "monster",
        "treasure",
        "nothing"
    ])

    if event == "monster":

        battle(
            player,
            random.choice(monsters)
        )

    elif event == "treasure":

        gold = random.randint(20, 100)

        player.gold += gold

        print(
            f"💰 Treasure found! "
            f"+{gold} gold"
        )

    else:

        print(
            "🚪 Empty room..."
        )

# Main Game Loop
while player.health > 0:

    print("\n===== DUNGEON =====")
    print("1. Explore")
    print("2. Show Stats")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        explore()

    elif choice == "2":
        player.show_stats()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")

if player.health <= 0:
    print("\n☠️ Game Over!")