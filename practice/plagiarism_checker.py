from difflib import SequenceMatcher
import os

# Read file content
def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return None

# Compare files
def compare_files(file1, file2):
    text1 = read_file(file1)
    text2 = read_file(file2)

    if text1 is None or text2 is None:
        print("One or both files not found.")
        return

    similarity = SequenceMatcher(
        None,
        text1,
        text2
    ).ratio()

    print("\n===== RESULT =====")
    print(f"Similarity: {similarity * 100:.2f}%")

    if similarity > 0.8:
        print("⚠️ High similarity detected")
    elif similarity > 0.5:
        print("⚠️ Moderate similarity detected")
    else:
        print("✅ Low similarity")

# Main Program
def main():
    print("===== CODE PLAGIARISM CHECKER =====")

    file1 = input("Enter first file path: ")
    file2 = input("Enter second file path: ")

    compare_files(file1, file2)

if __name__ == "__main__":
    main()