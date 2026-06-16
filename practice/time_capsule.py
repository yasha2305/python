import json
import os
from datetime import datetime

FILE = "capsule.json"

# Load capsules
def load_capsules():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# Save capsules
def save_capsules(capsules):
    with open(FILE, "w") as f:
        json.dump(capsules, f, indent=4)

# Create capsule
def create_capsule(capsules):

    title = input("Capsule Title: ")

    message = input("Secret Message: ")

    unlock_date = input(
        "Unlock Date (YYYY-MM-DD): "
    )

    capsules.append({
        "title": title,
        "message": message,
        "unlock_date": unlock_date
    })

    save_capsules(capsules)

    print("✅ Time Capsule Created")

# Open capsule
def open_capsule(capsules):

    today = datetime.now().date()

    found = False

    for capsule in capsules:

        unlock_date = datetime.strptime(
            capsule["unlock_date"],
            "%Y-%m-%d"
        ).date()

        if today >= unlock_date:

            print("\n📨", capsule["title"])
            print(capsule["message"])

            found = True

    if not found:
        print(
            "⏳ No capsules available yet."
        )

# View locked capsules
def view_capsules(capsules):

    if not capsules:
        print("No capsules stored.")
        return

    print("\n===== CAPSULES =====")

    for i, capsule in enumerate(
        capsules,
        start=1
    ):
        print(
            f"{i}. {capsule['title']} "
            f"(Unlocks: {capsule['unlock_date']})"
        )

# Main Program
def main():

    capsules = load_capsules()

    while True:

        print("\n===== DIGITAL TIME CAPSULE =====")
        print("1. Create Capsule")
        print("2. Open Available Capsules")
        print("3. View All Capsules")
        print("4. Exit")

        choice = input("Choice: ")

        if choice == "1":
            create_capsule(capsules)

        elif choice == "2":
            open_capsule(capsules)

        elif choice == "3":
            view_capsules(capsules)

        elif choice == "4":
            break

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()