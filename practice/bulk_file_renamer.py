import os

# Rename files
def rename_files(folder_path, prefix):

    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    files = os.listdir(folder_path)

    if not files:
        print("No files found.")
        return

    count = 1

    for file in files:

        old_path = os.path.join(folder_path, file)

        # Skip folders
        if os.path.isdir(old_path):
            continue

        extension = os.path.splitext(file)[1]

        new_name = f"{prefix}_{count}{extension}"

        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)

        print(f"Renamed: {file} → {new_name}")

        count += 1

    print("\nAll files renamed successfully!")

# Main program
def main():

    folder = input("Enter folder path: ").strip()

    prefix = input("Enter new file prefix: ").strip()

    if not prefix:
        print("Invalid prefix.")
        return

    rename_files(folder, prefix)

if __name__ == "__main__":
    main()