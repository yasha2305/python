import os
import hashlib

def get_hash(file_path):

    hasher = hashlib.md5()

    with open(file_path, "rb") as file:

        while chunk := file.read(4096):

            hasher.update(chunk)

    return hasher.hexdigest()

def find_duplicates(folder):

    hashes = {}
    duplicates = []

    for root, dirs, files in os.walk(folder):

        for file in files:

            path = os.path.join(root, file)

            try:

                file_hash = get_hash(path)

                if file_hash in hashes:

                    duplicates.append(
                        (path, hashes[file_hash])
                    )

                else:

                    hashes[file_hash] = path

            except:
                pass

    return duplicates

folder = input("Folder Path: ")

duplicates = find_duplicates(folder)

if duplicates:

    print("\n===== DUPLICATES FOUND =====\n")

    for dup, original in duplicates:

        print(f"Duplicate : {dup}")
        print(f"Original  : {original}")
        print("-" * 40)

else:

    print("No duplicates found.")