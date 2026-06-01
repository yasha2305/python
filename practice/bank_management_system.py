import sqlite3

# Database connection
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts(
    account_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    balance REAL NOT NULL
)
""")

conn.commit()

# Create Account
def create_account():
    acc_no = int(input("Account Number: "))
    name = input("Customer Name: ")
    balance = float(input("Initial Deposit: ₹"))

    cursor.execute(
        "INSERT INTO accounts VALUES (?, ?, ?)",
        (acc_no, name, balance)
    )

    conn.commit()
    print("✅ Account Created Successfully")

# View Account
def view_account():
    acc_no = int(input("Enter Account Number: "))

    cursor.execute(
        "SELECT * FROM accounts WHERE account_no=?",
        (acc_no,)
    )

    account = cursor.fetchone()

    if account:
        print("\n--- ACCOUNT DETAILS ---")
        print("Account No :", account[0])
        print("Name       :", account[1])
        print("Balance    : ₹", account[2])
    else:
        print("❌ Account Not Found")

# Deposit Money
def deposit():
    acc_no = int(input("Account Number: "))
    amount = float(input("Amount to Deposit: ₹"))

    cursor.execute(
        "UPDATE accounts SET balance = balance + ? WHERE account_no=?",
        (amount, acc_no)
    )

    conn.commit()
    print("✅ Deposit Successful")

# Withdraw Money
def withdraw():
    acc_no = int(input("Account Number: "))

    cursor.execute(
        "SELECT balance FROM accounts WHERE account_no=?",
        (acc_no,)
    )

    result = cursor.fetchone()

    if not result:
        print("❌ Account Not Found")
        return

    balance = result[0]

    amount = float(input("Amount to Withdraw: ₹"))

    if amount > balance:
        print("❌ Insufficient Balance")
        return

    cursor.execute(
        "UPDATE accounts SET balance = balance - ? WHERE account_no=?",
        (amount, acc_no)
    )

    conn.commit()
    print("✅ Withdrawal Successful")

# Delete Account
def delete_account():
    acc_no = int(input("Account Number: "))

    cursor.execute(
        "DELETE FROM accounts WHERE account_no=?",
        (acc_no,)
    )

    conn.commit()

    print("✅ Account Deleted")

# Show All Accounts
def show_all_accounts():

    cursor.execute("SELECT * FROM accounts")

    accounts = cursor.fetchall()

    print("\n--- ALL ACCOUNTS ---")

    for account in accounts:
        print(account)

# Main Menu
def main():

    while True:

        print("\n===== BANK MANAGEMENT SYSTEM =====")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Delete Account")
        print("6. Show All Accounts")
        print("7. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            view_account()

        elif choice == "3":
            deposit()

        elif choice == "4":
            withdraw()

        elif choice == "5":
            delete_account()

        elif choice == "6":
            show_all_accounts()

        elif choice == "7":
            conn.close()
            print("Goodbye!")
            break

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()