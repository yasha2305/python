import os
import shutil
import sqlite3

# Database Setup
conn = sqlite3.connect("cloud.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
""")

conn.commit()

CLOUD_FOLDER = "cloud_storage"

if not os.path.exists(CLOUD_FOLDER):
    os.makedirs(CLOUD_FOLDER)

# Register User
def register():

    username = input("Username: ")
    password = input("Password: ")

    try:

        cursor.execute(
            "INSERT INTO users VALUES (?, ?)",
            (username, password)
        )

        conn.commit()

        user_folder = os.path.join(
            CLOUD_FOLDER,
            username
        )

        os.makedirs(
            user_folder,
            exist_ok=True
        )

        print("✅ Registration Successful")

    except sqlite3.IntegrityError:

        print("❌ Username already exists")

# Login
def login():

    username = input("Username: ")
    password = input("Password: ")

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username=? AND password=?
        """,
        (username, password)
    )

    user = cursor.fetchone()

    if user:
        print("✅ Login Successful")
        return username

    print("❌ Invalid Credentials")
    return None

# Upload File
def upload_file(username):

    path = input(
        "Enter file path: "
    )

    if not os.path.exists(path):

        print("File not found.")
        return

    destination = os.path.join(
        CLOUD_FOLDER,
        username,
        os.path.basename(path)
    )

    shutil.copy2(
        path,
        destination
    )

    print("✅ File Uploaded")

# View Files
def view_files(username):

    folder = os.path.join(
        CLOUD_FOLDER,
        username
    )

    files = os.listdir(folder)

    print("\n===== YOUR FILES =====")

    if not files:

        print("No files uploaded.")

    else:

        for file in files:
            print(file)

# Download File
def download_file(username):

    filename = input(
        "Enter filename: "
    )

    source = os.path.join(
        CLOUD_FOLDER,
        username,
        filename
    )

    if not os.path.exists(source):

        print("File not found.")
        return

    destination = input(
        "Save location: "
    )

    shutil.copy2(
        source,
        destination
    )

    print("✅ File Downloaded")

# User Dashboard
def dashboard(username):

    while True:

        print(
            f"\n===== {username.upper()} CLOUD ====="
        )

        print("1. Upload File")
        print("2. View Files")
        print("3. Download File")
        print("4. Logout")

        choice = input("Choice: ")

        if choice == "1":
            upload_file(username)

        elif choice == "2":
            view_files(username)

        elif choice == "3":
            download_file(username)

        elif choice == "4":
            break

        else:
            print("Invalid Choice")

# Main Menu
def main():

    while True:

        print("\n===== MINI CLOUD STORAGE =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choice: ")

        if choice == "1":
            register()

        elif choice == "2":

            username = login()

            if username:
                dashboard(username)

        elif choice == "3":

            conn.close()
            print("Goodbye!")
            break

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()