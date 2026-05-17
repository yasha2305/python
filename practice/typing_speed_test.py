import time
import random

# Sentences for typing test
sentences = [
    "Python is a powerful programming language.",
    "Artificial intelligence is changing the world.",
    "Practice makes a person perfect.",
    "Typing speed improves with regular practice.",
    "Open source software helps developers learn."
]

# Calculate accuracy
def calculate_accuracy(original, typed):
    correct = 0

    for o, t in zip(original, typed):
        if o == t:
            correct += 1

    return (correct / len(original)) * 100

# Main typing test
def typing_test():
    sentence = random.choice(sentences)

    print("\n=== Typing Speed Test ===\n")
    print("Type the following sentence:\n")
    print(sentence)

    input("\nPress Enter when ready...")

    start_time = time.time()

    typed_text = input("\nStart typing:\n")

    end_time = time.time()

    # Time taken
    time_taken = end_time - start_time

    # Word count
    words = len(typed_text.split())

    # Calculate WPM
    wpm = (words / time_taken) * 60

    # Accuracy
    accuracy = calculate_accuracy(sentence, typed_text)

    print("\n--- RESULT ---")
    print(f"Time Taken : {time_taken:.2f} seconds")
    print(f"Typing Speed: {wpm:.2f} WPM")
    print(f"Accuracy   : {accuracy:.2f}%")

# Run program
if __name__ == "__main__":
    typing_test()