from cryptography.fernet import Fernet
import os

KEY_FILE = "filekey.key"

# Generate encryption key
def generate_key():
    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

# Load encryption key
def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()

    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

key = load_key()
cipher = Fernet(key)

# Encrypt file
def encrypt_file(filename):
    try:
        with open(filename, "rb") as file:
            file_data = file.read()

        encrypted_data = cipher.encrypt(file_data)

        with open(filename, "wb") as file:
            file.write(encrypted_data)

        print("✅ File encrypted successfully!")

    except FileNotFoundError:
        print("❌ File not found.")

# Decrypt file
def decrypt_file(filename):
    try:
        with open(filename, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = cipher.decrypt(encrypted_data)

        with open(filename, "wb") as file:
            file.write(decrypted_data)

        print("✅ File decrypted successfully!")

    except FileNotFoundError:
        print("❌ File not found.")

    except:
        print("❌ Invalid key or corrupted file.")

# Main menu
def main():
    while True:
        print("\n--- FILE ENCRYPTION TOOL ---")
        print("1. Encrypt File")
        print("2. Decrypt File")
        print("3. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            filename = input("Enter filename to encrypt: ")
            encrypt_file(filename)

        elif choice == "2":
            filename = input("Enter filename to decrypt: ")
            decrypt_file(filename)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()