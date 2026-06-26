import json
import os
import base64

FILE = "vault.json"

def encode(text):
    return base64.b64encode(
        text.encode()
    ).decode()

def decode(text):
    return base64.b64decode(
        text.encode()
    ).decode()

if os.path.exists(FILE):

    with open(FILE, "r") as file:
        vault = json.load(file)

else:
    vault = {}

while True:

    print("\n===== PASSWORD VAULT =====")
    print("1. Save Password")
    print("2. View Password")
    print("3. Show Websites")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":

        website = input("Website: ")
        username = input("Username: ")
        password = input("Password: ")

        vault[website] = {
            "username": encode(username),
            "password": encode(password)
        }

        with open(FILE, "w") as file:
            json.dump(vault, file, indent=4)

        print("Password Saved")

    elif choice == "2":

        website = input("Website: ")

        if website in vault:

            print(
                "Username:",
                decode(vault[website]["username"])
            )

            print(
                "Password:",
                decode(vault[website]["password"])
            )

        else:

            print("Website Not Found")

    elif choice == "3":

        for site in vault:
            print(site)

    elif choice == "4":
        break