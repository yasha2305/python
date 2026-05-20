import csv
import os
from datetime import datetime

FILE = "expenses.csv"

# Create CSV file if not exists
def initialize_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)

            writer.writerow([
                "Date",
                "Category",
                "Amount",
                "Description"
            ])

# Add expense
def add_expense():
    category = input("Enter category: ").strip()

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    description = input("Enter description: ").strip()

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)

        writer.writerow([
            date,
            category,
            amount,
            description
        ])

    print("Expense added successfully!")

# View expenses
def view_expenses():
    if not os.path.exists(FILE):
        print("No expense data found.")
        return

    with open(FILE, "r") as f:
        reader = csv.reader(f)

        print("\n--- EXPENSE LIST ---\n")

        for row in reader:
            print(row)

# Calculate total expenses
def total_expenses():
    total = 0

    if not os.path.exists(FILE):
        print("No expense data found.")
        return

    with open(FILE, "r") as f:
        reader = csv.reader(f)

        next(reader)  # Skip header

        for row in reader:
            total += float(row[2])

    print(f"\nTotal Expenses: ₹{total:.2f}")

# Main menu
def main():
    initialize_file()

    while True:
        print("\n--- EXPENSE TRACKER ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Expenses")
        print("4. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()