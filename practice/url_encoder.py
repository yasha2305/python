from urllib.parse import quote, unquote

while True:

    print("\n===== URL TOOL =====")
    print("1. Encode URL")
    print("2. Decode URL")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":

        text = input("Text: ")

        print("Encoded:")
        print(quote(text))

    elif choice == "2":

        text = input("Encoded URL: ")

        print("Decoded:")
        print(unquote(text))

    elif choice == "3":
        break