from PIL import Image
import pytesseract
import os

# For Windows (change path if needed)
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def extract_text(image_path):

    if not os.path.exists(image_path):
        print("Image not found.")
        return

    try:
        image = Image.open(image_path)

        text = pytesseract.image_to_string(image)

        print("\n===== EXTRACTED TEXT =====\n")
        print(text)

        with open(
            "extracted_text.txt",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(text)

        print(
            "\nText saved to extracted_text.txt"
        )

    except Exception as e:
        print("Error:", e)

def main():

    image_path = input(
        "Enter image path: "
    )

    extract_text(image_path)

if __name__ == "__main__":
    main()