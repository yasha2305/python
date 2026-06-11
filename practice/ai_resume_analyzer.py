import re

# Common skills list
SKILLS = [
    "python",
    "java",
    "c++",
    "sql",
    "html",
    "css",
    "javascript",
    "machine learning",
    "data analysis",
    "django",
    "flask",
    "git"
]

def analyze_resume(file_path):

    try:
        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            text = file.read().lower()

    except FileNotFoundError:
        print("Resume file not found.")
        return

    word_count = len(text.split())

    found_skills = []

    for skill in SKILLS:

        if skill in text:
            found_skills.append(skill)

    score = min(
        len(found_skills) * 10,
        100
    )

    email = re.findall(
        r'[\w\.-]+@[\w\.-]+',
        text
    )

    phone = re.findall(
        r'\d{10}',
        text
    )

    print("\n===== RESUME REPORT =====")

    print(f"Words        : {word_count}")
    print(f"Resume Score : {score}/100")

    print("\nSkills Found:")
    for skill in found_skills:
        print("✅", skill)

    print("\nEmail:")
    print(email[0] if email else "Not Found")

    print("\nPhone:")
    print(phone[0] if phone else "Not Found")

def main():

    path = input(
        "Resume text file path: "
    )

    analyze_resume(path)

if __name__ == "__main__":
    main()