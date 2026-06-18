import json
import os

SAVE_FILE = "pet_data.json"

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50

    def feed(self):
        self.hunger = max(0, self.hunger - 20)
        print(f"{self.name} has been fed! 🍖")

    def sleep(self):
        self.energy = min(100, self.energy + 30)
        print(f"{self.name} had a good sleep! 😴")

    def play(self):
        self.happiness = min(100, self.happiness + 20)
        self.energy = max(0, self.energy - 10)
        print(f"{self.name} is having fun! 🎾")

    def status(self):
        print("\n===== PET STATUS =====")
        print(f"Name      : {self.name}")
        print(f"Hunger    : {self.hunger}/100")
        print(f"Energy    : {self.energy}/100")
        print(f"Happiness : {self.happiness}/100")

    def update(self):
        self.hunger = min(100, self.hunger + 5)
        self.energy = max(0, self.energy - 5)
        self.happiness = max(0, self.happiness - 3)

def save_pet(pet):
    data = {
        "name": pet.name,
        "hunger": pet.hunger,
        "energy": pet.energy,
        "happiness": pet.happiness
    }

    with open(SAVE_FILE, "w") as file:
        json.dump(data, file)

def load_pet():
    if not os.path.exists(SAVE_FILE):
        return None

    with open(SAVE_FILE, "r") as file:
        data = json.load(file)

    pet = Pet(data["name"])
    pet.hunger = data["hunger"]
    pet.energy = data["energy"]
    pet.happiness = data["happiness"]

    return pet

# Main Program
pet = load_pet()

if pet is None:
    name = input("Enter Pet Name: ")
    pet = Pet(name)

while True:

    pet.update()

    print("\n===== VIRTUAL PET =====")
    print("1. Feed")
    print("2. Sleep")
    print("3. Play")
    print("4. Status")
    print("5. Save & Exit")

    choice = input("Choice: ")

    if choice == "1":
        pet.feed()

    elif choice == "2":
        pet.sleep()

    elif choice == "3":
        pet.play()

    elif choice == "4":
        pet.status()

    elif choice == "5":
        save_pet(pet)
        print("Pet Saved! 👋")
        break

    else:
        print("Invalid Choice")