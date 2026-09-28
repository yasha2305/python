import random

print("Welcome to Python!")

name = input("Enter your name: ")

number = random.randint(1, 100)

print(f"\nHello, {name}!")
print(f"Your random number is: {number}")

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

print("\nPython is fun! 🚀")