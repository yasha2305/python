import hashlib
import json
import os
import time

HASH_DB = "file_hashes.json"

# Generate SHA256 hash
def get_hash(file_path):
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as f:
            while True:
                chunk = f.read(4096)

                if not chunk:
                    break

                sha256.update(chunk)

        return sha256.hexdigest()

    except:
        return None

# Save hashes
def save_hashes(data):
    with open(HASH_DB, "w") as f:
        json.dump(data, f, indent=4)

# Load hashes
def load_hashes():
    if not os.path.exists(HASH_DB):
        return {}

    with open(HASH_DB, "r") as f:
        return json.load(f)

# Create baseline
def create_baseline(folder):
    hashes = {}

    for root, dirs, files in os.walk(folder):

        for file in files:

            path = os.path.join(root, file)

            file_hash = get_hash(path)

            if file_hash:
                hashes[path] = file_hash

    save_hashes(hashes)

    print("✅ Baseline Created")

# Check integrity
def check_integrity(folder):

    old_hashes = load_hashes()

    if not old_hashes:
        print(
            "No baseline found. "
            "Create baseline first."
        )
        return

    print("\nMonitoring Files...\n")

    while True:

        for root, dirs, files in os.walk(folder):

            for file in files:

                path = os.path.join(root, file)

                current_hash = get_hash(path)

                old_hash = old_hashes.get(path)

                if old_hash:

                    if current_hash != old_hash:

                        print(
                            f"⚠️ Modified: {path}"
                        )

                else:

                    print(
                        f"🆕 New File: {path}"
                    )

        time.sleep(5)

# Main Menu
def main():

    folder = input(
        "Folder to Monitor: "
    )

    while True:

        print(
            "\n===== FILE INTEGRITY MONITOR ====="
        )

        print("1. Create Baseline")
        print("2. Start Monitoring")
        print("3. Exit")

        choice = input("Choice: ")

        if choice == "1":
            create_baseline(folder)

        elif choice == "2":
            check_integrity(folder)

        elif choice == "3":
            break

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()