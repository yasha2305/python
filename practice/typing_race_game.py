import random
import time

sentences = [
    "Python is one of the most popular programming languages.",
    "Practice coding every day to improve your skills.",
    "Artificial intelligence is transforming the world.",
    "Success comes from consistency and hard work.",
    "Programming is the art of solving problems."
]

def typing_race():
    sentence = random.choice(sentences)

    print("\n===== TYPING RACE GAME =====")
    print("\nType the following sentence:\n")
    print(sentence)

    input("\nPress Enter to start...")

    start = time.time()

    user_text = input("\nType Here:\n")

    end = time.time()

    elapsed = end - start

    original_words = sentence.split()
    typed_words = user_text.split()

    correct = 0

    for i in range(
        min(len(original_words), len(typed_words))
    ):
        if original_words[i] == typed_words[i]:
            correct += 1

    accuracy = (
        correct / len(original_words)
    ) * 100

    wpm = (
        len(typed_words) / elapsed
    ) * 60

    print("\n===== RESULT =====")
    print(f"Time Taken : {elapsed:.2f} sec")
    print(f"Speed      : {wpm:.2f} WPM")
    print(f"Accuracy   : {accuracy:.2f}%")

while True:

    typing_race()

    choice = input(
        "\nPlay Again? (y/n): "
    ).lower()

    if choice != "y":
        print("Goodbye!")
        break