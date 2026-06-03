import sqlite3

# Database Connection
conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    emp_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL
)
""")

conn.commit()

# Add Employee
def add_employee():
    emp_id = int(input("Employee ID: "))
    name = input("Name: ")
    department = input("Department: ")
    salary = float(input("Salary: "))

    try:
        cursor.execute(
            "INSERT INTO employees VALUES (?, ?, ?, ?)",
            (emp_id, name, department, salary)
        )
        conn.commit()
        print("✅ Employee Added Successfully")
    except sqlite3.IntegrityError:
        print("❌ Employee ID already exists")

# View Employees
def view_employees():
    cursor.execute("SELECT * FROM employees")
    records = cursor.fetchall()

    if not records:
        print("No employee records found.")
        return

    print("\n--- EMPLOYEE LIST ---")
    for emp in records:
        print(emp)

# Search Employee
def search_employee():
    emp_id = int(input("Enter Employee ID: "))

    cursor.execute(
        "SELECT * FROM employees WHERE emp_id=?",
        (emp_id,)
    )

    emp = cursor.fetchone()

    if emp:
        print("\nEmployee Found:")
        print(emp)
    else:
        print("❌ Employee Not Found")

# Update Salary
def update_salary():
    emp_id = int(input("Employee ID: "))
    new_salary = float(input("New Salary: "))

    cursor.execute(
        "UPDATE employees SET salary=? WHERE emp_id=?",
        (new_salary, emp_id)
    )

    conn.commit()

    if cursor.rowcount:
        print("✅ Salary Updated")
    else:
        print("❌ Employee Not Found")

# Delete Employee
def delete_employee():
    emp_id = int(input("Employee ID: "))

    cursor.execute(
        "DELETE FROM employees WHERE emp_id=?",
        (emp_id,)
    )

    conn.commit()

    if cursor.rowcount:
        print("✅ Employee Deleted")
    else:
        print("❌ Employee Not Found")

# Department Report
def department_report():
    cursor.execute("""
    SELECT department,
           COUNT(*),
           AVG(salary)
    FROM employees
    GROUP BY department
    """)

    report = cursor.fetchall()

    print("\n--- DEPARTMENT REPORT ---")

    for dept, count, avg_salary in report:
        print(
            f"{dept} | Employees: {count} | "
            f"Avg Salary: ₹{avg_salary:.2f}"
        )

# Main Menu
def main():

    while True:

        print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Salary")
        print("5. Delete Employee")
        print("6. Department Report")
        print("7. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_salary()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            department_report()

        elif choice == "7":
            conn.close()
            print("Goodbye!")
            break

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main(