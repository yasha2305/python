import sqlite3

# Database Connection
conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS patients(
    patient_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    disease TEXT
)
""")

conn.commit()

# Add Patient
def add_patient():
    pid = int(input("Patient ID: "))
    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")
    disease = input("Disease: ")

    cursor.execute(
        "INSERT INTO patients VALUES (?, ?, ?, ?, ?)",
        (pid, name, age, gender, disease)
    )

    conn.commit()
    print("✅ Patient Added Successfully")

# View Patients
def view_patients():
    cursor.execute("SELECT * FROM patients")

    records = cursor.fetchall()

    if not records:
        print("No patient records found.")
        return

    print("\n--- PATIENT RECORDS ---")
    for patient in records:
        print(patient)

# Search Patient
def search_patient():
    pid = int(input("Enter Patient ID: "))

    cursor.execute(
        "SELECT * FROM patients WHERE patient_id=?",
        (pid,)
    )

    patient = cursor.fetchone()

    if patient:
        print("\nPatient Found:")
        print(patient)
    else:
        print("❌ Patient Not Found")

# Update Disease
def update_disease():
    pid = int(input("Patient ID: "))
    disease = input("New Disease: ")

    cursor.execute(
        "UPDATE patients SET disease=? WHERE patient_id=?",
        (disease, pid)
    )

    conn.commit()
    print("✅ Disease Updated")

# Delete Patient
def delete_patient():
    pid = int(input("Patient ID: "))

    cursor.execute(
        "DELETE FROM patients WHERE patient_id=?",
        (pid,)
    )

    conn.commit()
    print("✅ Patient Deleted")

# Main Menu
def main():

    while True:

        print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Update Disease")
        print("5. Delete Patient")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_patient()

        elif choice == "2":
            view_patients()

        elif choice == "3":
            search_patient()

        elif choice == "4":
            update_disease()

        elif choice == "5":
            delete_patient()

        elif choice == "6":
            conn.close()
            print("Goodbye!")
            break

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()