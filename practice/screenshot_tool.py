import pyautogui
from datetime import datetime
import os

# Folder to save screenshots
SAVE_FOLDER = "Screenshots"

# Create folder if not exists
os.makedirs(SAVE_FOLDER, exist_ok=True)

# Capture screenshot
def take_screenshot():

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = os.path.join(
        SAVE_FOLDER,
        f"screenshot_{timestamp}.png"
    )

    screenshot = pyautogui.screenshot()

    screenshot.save(filename)

    print(f"Screenshot saved: {filename}")

# Main menu
def main():

    while True:
        print("\n--- SCREENSHOT TOOL ---")
        print("1. Take Screenshot")
        print("2. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            take_screenshot()

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()