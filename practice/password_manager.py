from cryptography.fernet import Fernet
import json
import os

KEY_FILE = "secret.key"
DATA_FILE = "passwords.json"

# Generate key
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)

# Load key
def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()

    with open(KEY_FILE, "rb") as f:
        return f.read()

cipher = Fernet(load_key())

# Load passwords
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
def add_password():
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    encrypted = cipher.encrypt(password.encode()).decode()

    data = load_passwords()

    data[website] = {
        "username": username,
        "password": encrypted
    }

    save_passwords(data)

    print("✅ Password Saved")

# View password
def view_password():
    website = input("Website: ")

    data = load_passwords()

    if website not in data:
        print("❌ Website not found")
        return

    decrypted = cipher.decrypt(
        data[website]["password"].encode()
    ).decode()

    print("\n--- DETAILS ---")
    print("Username:", data[website]["username"])
    print("Password:", decrypted)

# Show websites
def show_websites():
    data = load_passwords()

    print("\nStored Websites:")
    for site in data:
        print("-", site)

# Main Menu
def main():

    while True:

        print("\n===== PASSWORD MANAGER =====")
        print("1. Add Password")
        print("2. View Password")
        print("3. Show Websites")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_password()

        elif choice == "2":
            view_password()

        elif choice == "3":
            show_websites()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()