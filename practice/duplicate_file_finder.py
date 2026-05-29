import os
import hashlib

# Generate file hash
def get_file_hash(filepath):

    hasher = hashlib.md5()

    try:
        with open(filepath, "rb") as file:

            while chunk := file.read(4096):
                hasher.update(chunk)

        return hasher.hexdigest()

    except:
        return None

# Find duplicate files
def find_duplicates(folder_path):

    hashes = {}
    duplicates = []

    for root, dirs, files in os.walk(folder_path):

        for file in files:

            filepath = os.path.join(root, file)

            file_hash = get_file_hash(filepath)

            if not file_hash:
                continue

            if file_hash in hashes:
                duplicates.append(
                    (filepath, hashes[file_hash])
                )

            else:
                hashes[file_hash] = filepath

    return duplicates

# Main program
def main():

    folder = input("Enter folder path: ").strip()

    if not os.path.exists(folder):
        print("Folder does not exist.")
        return

    print("\nScanning for duplicate files...\n")

    duplicates = find_duplicates(folder)

    if duplicates:

        print("Duplicate files found:\n")

        for dup, original in duplicates:

            print(f"Duplicate : {dup}")
            print(f"Original  : {original}")
            print("-" * 50)

    else:
        print("No duplicate files found.")

if __name__ == "__main__":
    main()