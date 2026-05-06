import string
import random
import json
import os

FILE = "url_db.json"
BASE_URL = "http://short.ly/"

# Load database
def load_db():
    if not os.path.exists(FILE):
        return {}
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {}

# Save database
def save_db(db):
    with open(FILE, "w") as f:
        json.dump(db, f, indent=4)

# Generate short code
def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# Shorten URL
def shorten_url(db):
    long_url = input("Enter long URL: ").strip()

    if not long_url:
        print("Invalid URL.")
        return

    code = generate_code()

    while code in db:
        code = generate_code()

    db[code] = long_url
    print("Short URL:", BASE_URL + code)

# Retrieve original URL
def retrieve_url(db):
    code = input("Enter short code: ").strip()

    if code in db:
        print("Original URL:", db[code])
    else:
        print("URL not found.")

# Main menu
def main():
    db = load_db()

    while True:
        print("\n--- URL SHORTENER ---")
        print("1. Shorten URL")
        print("2. Retrieve URL")
        print("3. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            shorten_url(db)
        elif choice == "2":
            retrieve_url(db)
        elif choice == "3":
            save_db(db)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()