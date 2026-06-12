import pyautogui
import time

# Safety feature
pyautogui.FAILSAFE = True

def auto_typing():

    text = input("Text to type: ")

    delay = int(
        input(
            "Start after how many seconds? "
        )
    )

    print(
        f"Switch to target window. "
        f"Starting in {delay} seconds..."
    )

    time.sleep(delay)

    pyautogui.write(
        text,
        interval=0.05
    )

    print("Typing completed!")

def auto_clicker():

    clicks = int(
        input(
            "Number of clicks: "
        )
    )

    delay = int(
        input(
            "Start after seconds: "
        )
    )

    print(
        f"Move cursor to target area. "
        f"Starting in {delay} seconds..."
    )

    time.sleep(delay)

    for _ in range(clicks):

        pyautogui.click()

    print("Clicking completed!")

def mouse_position():

    print(
        "Press Ctrl+C to stop."
    )

    try:

        while True:

            x, y = pyautogui.position()

            print(
                f"X={x} Y={y}",
                end="\r"
            )

            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nStopped.")

def main():

    while True:

        print(
            "\n===== DESKTOP AUTOMATION BOT ====="
        )

        print("1. Auto Typing")
        print("2. Auto Clicker")
        print("3. Show Mouse Position")
        print("4. Exit")

        choice = input("Choice: ")

        if choice == "1":
            auto_typing()

        elif choice == "2":
            auto_clicker()

        elif choice == "3":
            mouse_position()

        elif choice == "4":
            break

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()