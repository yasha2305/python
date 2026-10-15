
from datetime import datetime

accounts = {
    1001: {
        "name": "Vedant",
        "pin": "1234",
        "balance": 10000.00,
        "history": []
    },
    1002: {
        "name": "Rahul",
        "pin": "5678",
        "balance": 15000.00,
        "history": []
    },
    1003: {
        "name": "Aman",
        "pin": "4321",
        "balance": 20000.00,
        "history": []
    }
}


def record_transaction(account, message):
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    account["history"].append(f"{timestamp} | {message}")


def get_amount(prompt):
    try:
        amount = float(input(prompt))
        if amount <= 0:
            print("Please enter a positive amount.")
            return None
        return amount
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return None


def show_balance(account):
    print(f"\nAvailable Balance: Rs. {account['balance']:.2f}")


def deposit(account):
    amount = get_amount("Enter deposit amount: Rs. ")

    if amount is not None:
        account["balance"] += amount
        record_transaction(account, f"Deposited Rs. {amount:.2f}")
        print("Deposit successful!")


def withdraw(account):
    amount = get_amount("Enter withdrawal amount: Rs. ")

    if amount is not None:
        if amount > account["balance"]:
            print("Insufficient balance!")
        else:
            account["balance"] -= amount
            record_transaction(account, f"Withdrew Rs. {amount:.2f}")
            print("Please collect your cash.")


def transfer(account):
    try:
        receiver_number = int(input("Enter receiver account number: "))
    except ValueError:
        print("Invalid account number.")
        return

    if receiver_number not in accounts:
        print("Receiver account not found.")
        return

    receiver = accounts[receiver_number]

    if receiver is account:
        print("You cannot transfer money to your own account.")
        return

    amount = get_amount("Enter transfer amount: Rs. ")

    if amount is not None:
        if amount > account["balance"]:
            print("Insufficient balance!")
        else:
            account["balance"] -= amount
            receiver["balance"] += amount

            record_transaction(
                account,
                f"Transferred Rs. {amount:.2f} to {receiver['name']}"
            )
            record_transaction(
                receiver,
                f"Received Rs. {amount:.2f} from {account['name']}"
            )

            print("Money transferred successfully!")


def show_history(account):
    print("\n========== TRANSACTION HISTORY ==========")

    if not account["history"]:
        print("No transactions yet.")
        return

    for number, transaction in enumerate(account["history"], 1):
        print(f"{number}. {transaction}")


def atm():
    print("=" * 42)
    print("       SMART ATM BANKING SYSTEM")
    print("=" * 42)

    try:
        account_number = int(input("Enter account number: "))
    except ValueError:
        print("Invalid account number.")
        return

    if account_number not in accounts:
        print("Account not found!")
        return

    account = accounts[account_number]

    for attempt in range(3):
        pin = input("Enter your 4-digit PIN: ")

        if pin == account["pin"]:
            print(f"\nWelcome, {account['name']}!")
            break

        print("Incorrect PIN!")

    else:
        print("Too many failed attempts. Access denied.")
        return

    while True:
        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Transaction History")
        print("6. Account Details")
        print("7. Logout")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_balance(account)

        elif choice == "2":
            deposit(account)

        elif choice == "3":
            withdraw(account)

        elif choice == "4":
            transfer(account)

        elif choice == "5":
            show_history(account)

        elif choice == "6":
            print("\nAccount Holder:", account["name"])
            print("Account Number:", account_number)
            show_balance(account)

        elif choice == "7":
            print(f"Goodbye, {account['name']}!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    atm()
