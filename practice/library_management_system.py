import sqlite3

# Database connection
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    status TEXT DEFAULT 'Available'
)
""")

conn.commit()

# Add Book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    cursor.execute(
        "INSERT INTO books(title, author) VALUES (?, ?)",
        (title, author)
    )

    conn.commit()
    print("Book added successfully!")

# View Books
def view_books():
    cursor.execute("SELECT * FROM books")

    books = cursor.fetchall()

    if not books:
        print("No books available.")
        return

    print("\n--- BOOK LIST ---")

    for book in books:
        print(book)

# Issue Book
def issue_book():
    book_id = int(input("Enter Book ID: "))

    cursor.execute(
        "SELECT status FROM books WHERE id=?",
        (book_id,)
    )

    result = cursor.fetchone()

    if result and result[0] == "Available":

        cursor.execute(
            "UPDATE books SET status='Issued' WHERE id=?",
            (book_id,)
        )

        conn.commit()

        print("Book issued successfully!")

    else:
        print("Book unavailable.")

# Return Book
def return_book():
    book_id = int(input("Enter Book ID: "))

    cursor.execute(
        "UPDATE books SET status='Available' WHERE id=?",
        (book_id,)
    )

    conn.commit()

    print("Book returned successfully!")

# Delete Book
def delete_book():
    book_id = int(input("Enter Book ID to delete: "))

    cursor.execute(
        "DELETE FROM books WHERE id=?",
        (book_id,)
    )

    conn.commit()

    print("Book deleted successfully!")

# Main Menu
def main():

    while True:

        print("\n=== LIBRARY MANAGEMENT SYSTEM ===")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Delete Book")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            issue_book()

        elif choice == "4":
            return_book()

        elif choice == "5":
            delete_book()

        elif choice == "6":
            conn.close()
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()