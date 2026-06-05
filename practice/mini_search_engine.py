import os

# Build index
def build_index(folder_path):
    index = {}

    for file in os.listdir(folder_path):

        if file.endswith(".txt"):

            path = os.path.join(folder_path, file)

            try:
                with open(
                    path,
                    "r",
                    encoding="utf-8"
                ) as f:

                    content = f.read().lower()

                    words = content.split()

                    for word in words:

                        if word not in index:
                            index[word] = set()

                        index[word].add(file)

            except Exception as e:
                print(f"Error reading {file}: {e}")

    return index

# Search word
def search(index):

    while True:

        keyword = input(
            "\nSearch keyword (exit to quit): "
        ).lower()

        if keyword == "exit":
            break

        if keyword in index:

            print("\nFound in files:")

            for file in index[keyword]:
                print("📄", file)

        else:
            print("No results found.")

# Main
def main():

    folder = input(
        "Enter folder containing text files: "
    )

    if not os.path.exists(folder):
        print("Folder not found.")
        return

    print("\nBuilding search index...")

    index = build_index(folder)

    print(
        f"Indexed {len(index)} unique words."
    )

    search(index)

if __name__ == "__main__":
    main()