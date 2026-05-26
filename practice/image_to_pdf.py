from PIL import Image
import os

# Convert images to PDF
def convert_to_pdf(image_paths, output_pdf):

    images = []

    for path in image_paths:

        if not os.path.exists(path):
            print(f"File not found: {path}")
            continue

        img = Image.open(path)

        # Convert to RGB
        if img.mode == "RGBA":
            img = img.convert("RGB")

        images.append(img)

    if not images:
        print("No valid images found.")
        return

    # Save first image and append others
    images[0].save(
        output_pdf,
        save_all=True,
        append_images=images[1:]
    )

    print(f"\nPDF created successfully: {output_pdf}")

# Main program
def main():

    print("=== IMAGE TO PDF CONVERTER ===\n")

    image_paths = []

    while True:

        path = input(
            "Enter image path "
            "(or type 'done'): "
        ).strip()

        if path.lower() == "done":
            break

        image_paths.append(path)

    if not image_paths:
        print("No images provided.")
        return

    output_pdf = input(
        "Enter output PDF name: "
    ).strip()

    if not output_pdf.endswith(".pdf"):
        output_pdf += ".pdf"

    convert_to_pdf(image_paths, output_pdf)

if __name__ == "__main__":
    main()