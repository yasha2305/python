import os
import shutil
from datetime import datetime

VERSIONS_DIR = "versions"

os.makedirs(VERSIONS_DIR, exist_ok=True)

def save_version():

    file_name = input(
        "File name: "
    )

    if not os.path.exists(file_name):

        print("File not found.")
        return

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    version_name = (
        f"{timestamp}_{file_name}"
    )

    shutil.copy(
        file_name,
        os.path.join(
            VERSIONS_DIR,
            version_name
        )
    )

    print("✅ Version Saved")

def show_versions():

    files = os.listdir(
        VERSIONS_DIR
    )

    if not files:

        print("No versions found.")
        return

    print("\n===== VERSIONS =====")

    for i, file in enumerate(files, 1):

        print(f"{i}. {file}")

def restore_version():

    files = os.listdir(
        VERSIONS_DIR
    )

    show_versions()

    try:

        choice = int(
            input(
                "\nVersion Number: "
            )
        )

        selected = files[
            choice - 1
        ]

        original_name = (
            selected.split("_", 2)[2]
        )

        shutil.copy(
            os.path.join(
                VERSIONS_DIR,
                selected
            ),
            original_name
        )

        print(
            "✅ File Restored"
        )

    except:

        print(
            "Invalid Choice"
        )

while True:

    print(
        "\n===== MINI VERSION CONTROL ====="
    )

    print("1. Save Version")
    print("2. Show Versions")
    print("3. Restore Version")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":
        save_version()

    elif choice == "2":
        show_versions()

    elif choice == "3":
        restore_version()

    elif choice == "4":
        break

    else:
        print("Invalid Choice")