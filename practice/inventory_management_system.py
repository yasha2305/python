import sqlite3

# Database Setup
conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
)
""")

conn.commit()

# Add Product
def add_product():
    pid = int(input("Product ID: "))
    name = input("Product Name: ")
    qty = int(input("Quantity: "))
    price = float(input("Price: "))

    try:
        cursor.execute(
            "INSERT INTO products VALUES (?, ?, ?, ?)",
            (pid, name, qty, price)
        )

        conn.commit()
        print("✅ Product Added Successfully")

    except sqlite3.IntegrityError:
        print("❌ Product ID Already Exists")

# View Products
def view_products():

    cursor.execute(
        "SELECT * FROM products"
    )

    products = cursor.fetchall()

    if not products:
        print("No products available.")
        return

    print("\n===== PRODUCT LIST =====")

    for product in products:
        print(product)

# Search Product
def search_product():

    pid = int(
        input("Enter Product ID: ")
    )

    cursor.execute(
        "SELECT * FROM products WHERE product_id=?",
        (pid,)
    )

    product = cursor.fetchone()

    if product:
        print("\nProduct Found:")
        print(product)
    else:
        print("❌ Product Not Found")

# Update Stock
def update_stock():

    pid = int(
        input("Product ID: ")
    )

    qty = int(
        input("New Quantity: ")
    )

    cursor.execute(
        """
        UPDATE products
        SET quantity=?
        WHERE product_id=?
        """,
        (qty, pid)
    )

    conn.commit()

    if cursor.rowcount:
        print("✅ Stock Updated")
    else:
        print("❌ Product Not Found")

# Delete Product
def delete_product():

    pid = int(
        input("Product ID: ")
    )

    cursor.execute(
        "DELETE FROM products WHERE product_id=?",
        (pid,)
    )

    conn.commit()

    if cursor.rowcount:
        print("✅ Product Deleted")
    else:
        print("❌ Product Not Found")

# Inventory Value Report
def inventory_report():

    cursor.execute("""
    SELECT
    SUM(quantity * price)
    FROM products
    """)

    total = cursor.fetchone()[0]

    print(
        "\nTotal Inventory Value: ₹",
        total if total else 0
    )

# Main Menu
def main():

    while True:

        print("\n===== INVENTORY SYSTEM =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Stock")
        print("5. Delete Product")
        print("6. Inventory Report")
        print("7. Exit")

        choice = input("Choice: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_stock()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            inventory_report()

        elif choice == "7":
            conn.close()
            print("Goodbye!")
            break

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()