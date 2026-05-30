import sqlite3
from datetime import datetime

# Create database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    category TEXT,
    description TEXT,
    expense_date TEXT
)
""")

conn.commit()

# Add expense
def add_expense():
    amount = float(input("Amount: ₹"))
    category = input("Category: ")
    description = input("Description: ")

    date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
    INSERT INTO expenses
    (amount, category, description, expense_date)
    VALUES (?, ?, ?, ?)
    """, (amount, category, description, date))

    conn.commit()
    print("Expense added successfully!")

# View all expenses
def view_expenses():
    cursor.execute("SELECT * FROM expenses")

    rows = cursor.fetchall()

    if not rows:
        print("No expenses found.")
        return

    print("\n--- EXPENSES ---")

    for row in rows:
        print(row)

# Monthly report
def monthly_report():

    month = input("Enter month (YYYY-MM): ")

    cursor.execute("""
    SELECT SUM(amount)
    FROM expenses
    WHERE expense_date LIKE ?
    """, (month + "%",))

    total = cursor.fetchone()[0]

    print(
        f"\nTotal expenses for {month}: "
        f"₹{total if total else 0}"
    )

# Category report
def category_report():

    cursor.execute("""
    SELECT category, SUM(amount)
    FROM expenses
    GROUP BY category
    """)

    rows = cursor.fetchall()

    print("\n--- CATEGORY REPORT ---")

    for category, total in rows:
        print(f"{category}: ₹{total}")

# Main menu
def main():

    while True:

        print("\n=== EXPENSE TRACKER ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Report")
        print("4. Category Report")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            monthly_report()

        elif choice == "4":
            category_report()

        elif choice == "5":
            conn.close()
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()