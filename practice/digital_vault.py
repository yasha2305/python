import base64
import json
import os

FILE = "vault.json"

# Load notes
def load_notes():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

# Save notes
def save_notes(notes):
    with open(FILE, "w") as f:
        json.dump(notes, f, indent=4)

# Encode note
def encrypt(text):
    return base64.b64encode(
        text.encode()
    ).decode()

# Decode note
def decrypt(text):
    return base64.b64decode(
        text.encode()
    ).decode()

# Add secret note
def add_note(notes):

    title = input("Title: ")
    content = input("Secret Note: ")

    notes[title] = encrypt(content)

    save_notes(notes)

    print("✅ Note Saved")

# View secret note
def view_note(notes):

    title = input("Title: ")

    if title in notes:

        print(
            "\nSecret Content:"
        )

        print(
            decrypt(notes[title])
        )

    else:

        print("❌ Note Not Found")

# Show note titles
def list_notes(notes):

    if not notes:

        print("No notes found.")
        return

    print("\n===== NOTES =====")

    for title in notes:
        print("📄", title)

# Delete note
def delete_note(notes):

    title = input("Title: ")

    if title in notes:

        del notes[title]

        save_notes(notes)

        print("✅ Deleted")

    else:

        print("❌ Note Not Found")

# Main Program
def main():

    notes = load_notes()

    while True:

        print("\n===== DIGITAL VAULT =====")
        print("1. Add Secret Note")
        print("2. View Secret Note")
        print("3. List Notes")
        print("4. Delete Note")
        print("5. Exit")

        choice = input("Choice: ")

        if choice == "1":
            add_note(notes)

        elif choice == "2":
            view_note(notes)

        elif choice == "3":
            list_notes(notes)

        elif choice == "4":
            delete_note(notes)

        elif choice == "5":
            break

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()