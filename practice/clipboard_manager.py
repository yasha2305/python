import pyperclip
import time
import json
import os

FILE = "clipboard_history.json"

# Load clipboard history
def load_history():
    if not os.path.exists(FILE):
        return []

    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

# Save clipboard history
def save_history(history):
    with open(FILE, "w") as f:
        json.dump(history, f, indent=4)

# Monitor clipboard
def monitor_clipboard():
    history = load_history()

    last_text = ""

    print("Clipboard monitoring started...")
    print("Press Ctrl + C to stop.\n")

    try:
        while True:
            current_text = pyperclip.paste()

            if current_text != last_text and current_text.strip():
                print("Copied:", current_text)

                history.append(current_text)

                save_history(history)

                last_text = current_text

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

# Show history
def show_history():
    history = load_history()

    if not history:
        print("No clipboard history found.")
        return

    print("\n--- Clipboard History ---\n")

    for i, item in enumerate(history, start=1):
        print(f"{i}. {item}")

# Main menu
def main():
    while True:
        print("\n--- CLIPBOARD MANAGER ---")
        print("1. Start Monitoring")
        print("2. Show Clipboard History")
        print("3. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            monitor_clipboard()

        elif choice == "2":
            show_history()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()