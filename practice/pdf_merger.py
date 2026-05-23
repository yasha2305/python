from PyPDF2 import PdfMerger
import os

# Merge PDFs
def merge_pdfs(pdf_list, output_file):

    merger = PdfMerger()

    for pdf in pdf_list:

        if os.path.exists(pdf):
            merger.append(pdf)
            print(f"Added: {pdf}")

        else:
            print(f"File not found: {pdf}")

    merger.write(output_file)
    merger.close()

    print(f"\nMerged PDF saved as: {output_file}")

# Main program
def main():

    print("=== PDF MERGER TOOL ===\n")

    pdfs = []

    while True:
        pdf = input(
            "Enter PDF file path "
            "(or type 'done'): "
        ).strip()

        if pdf.lower() == "done":
            break

        pdfs.append(pdf)

    if not pdfs:
        print("No PDF files provided.")
        return

    output = input(
        "Enter output PDF name: "
    ).strip()

    if not output.endswith(".pdf"):
        output += ".pdf"

    merge_pdfs(pdfs, output)

if __name__ == "__main__":
    main()
    