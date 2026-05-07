from cryptography.fernet import Fernet
import json
import os

KEY_FILE = "secret.key"
DATA_FILE = "passwords.json"

# Generate encryption key
def generate_key():
    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as f:
        f.write(key)

# Load encryption key
def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()

    with open(KEY_FILE, "rb") as f:
        return f.read()

key = load_key()
cipher = Fernet(key)

# Load saved passwords
def load_passwords():
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

# Save passwords
def save_passwords(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Add password
def add_password(data):
    website = input("Enter website: ").strip()
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    encrypted_password = cipher.encrypt(password.encode()).decode()

    data[website] = {
        "username": username,
        "password": encrypted_password
    }

    print("Password saved securely!")

# Retrieve password
def get_password(data):
    website = input("Enter website: ").strip()

    if website in data:
        encrypted_password = data[website]["password"]

        decrypted_password = cipher.decrypt(
            encrypted_password.encode()
        ).decode()

        print("\nWebsite :", website)
        print("Username:", data[website]["username"])
        print("Password:", decrypted_password)

    else:
        print("No data found.")

# Main menu
def main():
    data = load_passwords()

    while True:
        print("\n--- PASSWORD MANAGER ---")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            add_password(data)

        elif choice == "2":
            get_password(data)

        elif choice == "3":
            save_passwords(data)
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()