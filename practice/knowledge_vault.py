import sqlite3

# Database Setup
conn = sqlite3.connect("knowledge_vault.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS notes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    tags TEXT
)
""")

conn.commit()

# Add Note
def add_note():

    title = input("Title: ")
    content = input("Content: ")
    tags = input(
        "Tags (comma separated): "
    )

    cursor.execute(
        """
        INSERT INTO notes
        (title, content, tags)
        VALUES (?, ?, ?)
        """,
        (title, content, tags)
    )

    conn.commit()

    print("✅ Note Saved")

# View Notes
def view_notes():

    cursor.execute(
        "SELECT * FROM notes"
    )

    notes = cursor.fetchall()

    if not notes:
        print("No notes available.")
        return

    print("\n===== NOTES =====")

    for note in notes:

        print(f"\nID: {note[0]}")
        print(f"Title: {note[1]}")
        print(f"Tags: {note[3]}")
        print(f"Content: {note[2]}")

# Search Notes
def search_notes():

    keyword = input(
        "Search keyword/tag: "
    )

    cursor.execute(
        """
        SELECT * FROM notes
        WHERE title LIKE ?
        OR content LIKE ?
        OR tags LIKE ?
        """,
        (
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%"
        )
    )

    results = cursor.fetchall()

    if not results:
        print("No matching notes.")
        return

    print("\n===== RESULTS =====")

    for note in results:

        print(f"\nTitle: {note[1]}")
        print(f"Tags: {note[3]}")
        print(f"Content: {note[2]}")

# Delete Note
def delete_note():

    note_id = int(
        input("Note ID: ")
    )

    cursor.execute(
        "DELETE FROM notes WHERE id=?",
        (note_id,)
    )

    conn.commit()

    if cursor.rowcount:
        print("✅ Note Deleted")
    else:
        print("❌ Note Not Found")

# Main Menu
while True:

    print("\n===== KNOWLEDGE VAULT =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Search Notes")
    print("4. Delete Note")
    print("5. Exit")

    choice = input("Choice: ")

    if choice == "1":
        add_note()

    elif choice == "2":
        view_notes()

    elif choice == "3":
        search_notes()

    elif choice == "4":
        delete_note()

    elif choice == "5":
        conn.close()
        break

    else:
        print("Invalid Choice")