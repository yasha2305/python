import json
import time
import os

DATA_FILE = "user_profile.json"

# Save profile
def save_profile(profile):
    with open(DATA_FILE, "w") as file:
        json.dump(profile, file)

# Load profile
def load_profile():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return None

# Register user
def register():

    password = input(
        "Create Password: "
    )

    print(
        "\nType the password again naturally..."
    )

    start = time.time()

    confirm = input(
        "Password: "
    )

    end = time.time()

    if password != confirm:

        print(
            "Passwords do not match."
        )

        return

    typing_time = end - start

    profile = {
        "password": password,
        "typing_time": typing_time
    }

    save_profile(profile)

    print(
        "✅ Profile Created"
    )

# Login
def login():

    profile = load_profile()

    if not profile:

        print(
            "No profile found."
        )

        return

    print(
        "\nLogin using your password"
    )

    start = time.time()

    entered = input(
        "Password: "
    )

    end = time.time()

    if entered != profile["password"]:

        print(
            "❌ Wrong Password"
        )

        return

    current_time = end - start

    stored_time = profile["typing_time"]

    difference = abs(
        current_time - stored_time
    )

    if difference < 2:
        print(
            "✅ Authentication Successful"
        )
    else:
        print(
            "⚠️ Password Correct "
            "but typing pattern differs"
        )

# Main
while True:

    print(
        "\n===== TYPING AUTH SYSTEM ====="
    )

    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        break

    else:
        print("Invalid Choice")