#this program will calculate your grade(grade calculator)
marks = list(map(int, input("Enter marks separated by space: ").split()))
average = sum(marks) / len(marks)

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "Fail"

print("Average:", average)
print("Grade:", grade)
