import sqlite3

# Connect database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    roll_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    course TEXT NOT NULL,
    marks REAL
)
""")
conn.commit()

# Add student
def add_student():
    roll = int(input("Roll No: "))
    name = input("Name: ")
    course = input("Course: ")
    marks = float(input("Marks: "))

    cursor.execute(
        "INSERT INTO students VALUES (?, ?, ?, ?)",
        (roll, name, course, marks)
    )
    conn.commit()
    print("Student added successfully!")

# View students
def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if not rows:
        print("No records found.")
        return

    print("\n--- STUDENT RECORDS ---")
    for row in rows:
        print(row)

# Search student
def search_student():
    roll = int(input("Enter Roll No: "))

    cursor.execute(
        "SELECT * FROM students WHERE roll_no=?",
        (roll,)
    )

    student = cursor.fetchone()

    if student:
        print("\nStudent Found:")
        print(student)
    else:
        print("Student not found.")

# Update marks
def update_marks():
    roll = int(input("Enter Roll No: "))
    marks = float(input("New Marks: "))

    cursor.execute(
        "UPDATE students SET marks=? WHERE roll_no=?",
        (marks, roll)
    )

    conn.commit()
    print("Marks updated!")

# Delete student
def delete_student():
    roll = int(input("Enter Roll No: "))

    cursor.execute(
        "DELETE FROM students WHERE roll_no=?",
        (roll,)
    )

    conn.commit()
    print("Student deleted!")

# Topper report
def show_topper():
    cursor.execute("""
        SELECT * FROM students
        ORDER BY marks DESC
        LIMIT 1
    """)

    topper = cursor.fetchone()

    if topper:
        print("\n🏆 TOPPER")
        print(topper)
    else:
        print("No records available.")

# Main menu
def main():

    while True:

        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Show Topper")
        print("7. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_marks()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            show_topper()

        elif choice == "7":
            conn.close()
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()