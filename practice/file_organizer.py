import os
import shutil

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

# Organize files
def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    files = os.listdir(folder_path)

    for file in files:
        file_path = os.path.join(folder_path, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        # File extension
        _, extension = os.path.splitext(file)

        moved = False

        # Match file type
        for folder_name, extensions in FILE_TYPES.items():

            if extension.lower() in extensions:

                target_folder = os.path.join(
                    folder_path,
                    folder_name
                )

                # Create folder if not exists
                os.makedirs(target_folder, exist_ok=True)

                # Move file
                shutil.move(
                    file_path,
                    os.path.join(target_folder, file)
                )

                print(f"Moved: {file} → {folder_name}")

                moved = True
                break

        # Other files
        if not moved:
            other_folder = os.path.join(folder_path, "Others")

            os.makedirs(other_folder, exist_ok=True)

            shutil.move(
                file_path,
                os.path.join(other_folder, file)
            )

            print(f"Moved: {file} → Others")

# Main program
def main():
    folder = input("Enter folder path: ").strip()

    organize_folder(folder)

    print("\nFile organization completed!")

if __name__ == "__main__":
    main()