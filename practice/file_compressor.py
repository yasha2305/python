import zipfile
import os

def compress_file():

    file_path = input(
        "Enter file path: "
    )

    if not os.path.exists(file_path):
        print("File not found!")
        return

    zip_name = input(
        "ZIP file name: "
    ) + ".zip"

    with zipfile.ZipFile(
        zip_name,
        "w",
        zipfile.ZIP_DEFLATED
    ) as zipf:

        zipf.write(
            file_path,
            os.path.basename(file_path)
        )

    print(
        f"✅ Compressed to {zip_name}"
    )

def extract_zip():

    zip_name = input(
        "ZIP file name: "
    )

    extract_folder = input(
        "Extract folder: "
    )

    with zipfile.ZipFile(
        zip_name,
        "r"
    ) as zipf:

        zipf.extractall(
            extract_folder
        )

    print("✅ Extraction Complete")

while True:

    print("\n===== FILE COMPRESSOR =====")
    print("1. Compress File")
    print("2. Extract ZIP")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        compress_file()

    elif choice == "2":
        extract_zip()

    elif choice == "3":
        break

    else:
        print("Invalid Choice")