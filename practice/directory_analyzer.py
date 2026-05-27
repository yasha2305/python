import os

# Convert bytes to readable format
def format_size(size):

    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:

        if size < 1024:
            return f"{size:.2f} {unit}"

        size /= 1024

# Analyze directory
def analyze_directory(folder_path):

    total_size = 0
    total_files = 0
    total_folders = 0

    largest_files = []

    for root, dirs, files in os.walk(folder_path):

        total_folders += len(dirs)

        for file in files:

            file_path = os.path.join(root, file)

            try:
                size = os.path.getsize(file_path)

                total_size += size
                total_files += 1

                largest_files.append((size, file_path))

            except:
                pass

    # Sort by size descending
    largest_files.sort(reverse=True)

    print("\n--- DIRECTORY REPORT ---\n")

    print(f"Folder: {folder_path}")
    print(f"Total Size   : {format_size(total_size)}")
    print(f"Total Files  : {total_files}")
    print(f"Total Folders: {total_folders}")

    print("\nTop 5 Largest Files:\n")

    for size, path in largest_files[:5]:
        print(f"{format_size(size)} → {path}")

# Main program
def main():

    folder = input("Enter folder path: ").strip()

    if not os.path.exists(folder):
        print("Folder does not exist.")
        return

    analyze_directory(folder)

if __name__ == "__main__":
    main()