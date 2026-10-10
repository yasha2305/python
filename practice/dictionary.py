
dictionary = {}

while True:
    print("\n===== MY DICTIONARY =====")
    print("1. Add Word")
    print("2. Search Word")
    print("3. Update Meaning")
    print("4. Delete Word")
    print("5. Display All Words")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        word = input("Enter word: ").lower()
        meaning = input("Enter meaning: ")
        dictionary[word] = meaning
        print("Word added successfully!")

    elif choice == "2":
        word = input("Enter word to search: ").lower()
        if word in dictionary:
            print("Meaning:", dictionary[word])
        else:
            print("Word not found!")

    elif choice == "3":
        word = input("Enter word to update: ").lower()
        if word in dictionary:
            dictionary[word] = input("Enter new meaning: ")
            print("Meaning updated!")
        else:
            print("Word not found!")

    elif choice == "4":
        word = input("Enter word to delete: ").lower()
        if word in dictionary:
            del dictionary[word]
            print("Word deleted!")
        else:
            print("Word not found!")

    elif choice == "5":
        if dictionary:
            for word, meaning in dictionary.items():
                print(word, ":", meaning)
        else:
            print("Dictionary is empty!")

    elif choice == "6":
        print("Thank you for using the dictionary!")
        break

    else:
        print("Invalid choice! Try again.")