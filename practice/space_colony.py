import random

food = 100
oxygen = 100
energy = 100
colonists = 10
day = 1

while True:

    print(f"\n===== DAY {day} =====")
    print(f"👨 Colonists : {colonists}")
    print(f"🍞 Food      : {food}")
    print(f"🌬 Oxygen    : {oxygen}")
    print(f"⚡ Energy    : {energy}")

    print("\n1. Farm Food")
    print("2. Generate Oxygen")
    print("3. Produce Energy")
    print("4. Recruit Colonist")
    print("5. End Day")
    print("6. Exit")

    choice = input("Choice: ")

    if choice == "1":
        food += random.randint(10, 30)

    elif choice == "2":
        oxygen += random.randint(10, 25)

    elif choice == "3":
        energy += random.randint(10, 25)

    elif choice == "4":

        if food >= 10 and oxygen >= 10:
            colonists += 1
            food -= 10
            oxygen -= 10

    elif choice == "5":

        day += 1

        food -= colonists * 2
        oxygen -= colonists
        energy -= colonists

        event = random.choice([
            "none",
            "meteor",
            "supply",
            "solar"
        ])

        if event == "meteor":

            damage = random.randint(5, 20)

            energy -= damage

            print(
                f"\n☄ Meteor Strike!"
                f" Lost {damage} energy"
            )

        elif event == "supply":

            bonus = random.randint(20, 50)

            food += bonus

            print(
                f"\n📦 Supply Ship!"
                f" +{bonus} food"
            )

        elif event == "solar":

            bonus = random.randint(10, 30)

            energy += bonus

            print(
                f"\n☀ Solar Boost!"
                f" +{bonus} energy"
            )

        if (
            food <= 0 or
            oxygen <= 0 or
            energy <= 0
        ):
            print(
                "\n💀 Colony Failed!"
            )
            break

    elif choice == "6":
        break

    else:
        print("Invalid Choice")