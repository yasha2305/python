from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def create_invoice():

    customer = input("Customer Name: ")
    invoice_no = input("Invoice Number: ")

    pdf = SimpleDocTemplate(
        f"Invoice_{invoice_no}.pdf"
    )

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(
        "INVOICE",
        styles["Title"]
    )

    content.append(title)
    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            f"Customer: {customer}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Invoice No: {invoice_no}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 20))

    items = [
        ["Item", "Qty", "Price"]
    ]

    total = 0

    while True:

        item = input(
            "Item Name (done to finish): "
        )

        if item.lower() == "done":
            break

        qty = int(input("Quantity: "))
        price = float(input("Price: "))

        total += qty * price

        items.append(
            [item, str(qty), f"₹{price}"]
        )

    items.append(
        ["TOTAL", "", f"₹{total}"]
    )

    table = Table(items)

    table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.lightgrey
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                1,
                colors.black
            )
        ])
    )

    content.append(table)

    pdf.build(content)

    print(
        f"Invoice saved as "
        f"Invoice_{invoice_no}.pdf"
    )

if __name__ == "__main__":
    create_invoice()