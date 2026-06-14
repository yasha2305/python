import sqlite3
import matplotlib.pyplot as plt

# Database Setup
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    amount REAL
)
""")

conn.commit()

# Add Expense
def add_expense():

    category = input(
        "Category: "
    )

    amount = float(
        input(
            "Amount: ₹"
        )
    )

    cursor.execute(
        """
        INSERT INTO expenses
        (category, amount)
        VALUES (?, ?)
        """,
        (category, amount)
    )

    conn.commit()

    print("Expense Added!")

# View Expenses
def view_expenses():

    cursor.execute(
        "SELECT * FROM expenses"
    )

    records = cursor.fetchall()

    if not records:

        print("No expenses found.")
        return

    print("\n===== EXPENSES =====")

    for row in records:
        print(row)

# Expense Chart
def show_chart():

    cursor.execute("""
    SELECT category,
           SUM(amount)
    FROM expenses
    GROUP BY category
    """)

    data = cursor.fetchall()

    if not data:

        print("No data available.")
        return

    categories = [x[0] for x in data]
    amounts = [x[1] for x in data]

    plt.figure(figsize=(7, 7))

    plt.pie(
        amounts,
        labels=categories,
        autopct="%1.1f%%"
    )

    plt.title(
        "Expense Distribution"
    )

    plt.show()

# Main Menu
while True:

    print(
        "\n===== SMART EXPENSE TRACKER ====="
    )

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Chart")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_chart()

    elif choice == "4":
        break

    else:
        print("Invalid Choice")

conn.close()