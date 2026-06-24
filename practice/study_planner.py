subjects = []

print("===== AI STUDY PLANNER =====")

n = int(input("How many subjects? "))

for i in range(n):

    subject = input(
        f"Subject {i+1}: "
    )

    subjects.append(subject)

hours = float(
    input(
        "Available study hours per day: "
    )
)

time_per_subject = (
    hours / len(subjects)
)

print("\n===== TODAY'S PLAN =====\n")

for subject in subjects:

    print(
        f"📖 {subject}"
    )

    print(
        f"Study Time: "
        f"{time_per_subject:.1f} Hours\n"
    )

print("✅ Plan Generated")