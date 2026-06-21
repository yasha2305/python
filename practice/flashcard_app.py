import json
import os
import random

FILE = "flashcards.json"

def load_cards():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_cards(cards):
    with open(FILE, "w") as f:
        json.dump(cards, f, indent=4)

cards = load_cards()

while True:

    print("\n===== FLASHCARD APP =====")
    print("1. Add Flashcard")
    print("2. Study Mode")
    print("3. View All")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":

        question = input("Question: ")
        answer = input("Answer: ")

        cards[question] = answer

        save_cards(cards)

        print("✅ Flashcard Saved")

    elif choice == "2":

        if not cards:
            print("No flashcards found.")
            continue

        question = random.choice(
            list(cards.keys())
        )

        print("\nQuestion:")
        print(question)

        input("\nPress Enter for Answer...")

        print(
            "Answer:",
            cards[question]
        )

    elif choice == "3":

        for q, a in cards.items():

            print(
                f"\nQ: {q}"
            )

            print(
                f"A: {a}"
            )

    elif choice == "4":
        break

    else:
        print("Invalid Choice")