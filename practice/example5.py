# Comparison and Logical Operators

age1 = int(input("Enter first person's age: "))
age2 = int(input("Enter second person's age: "))

print("age1 == age2 :", age1 == age2)
print("age1 != age2 :", age1 != age2)
print("age1 > age2 :", age1 > age2)
print("age1 < age2 :", age1 < age2)
print("age1 >= age2 :", age1 >= age2)
print("age1 <= age2 :", age1 <= age2)

print("Both eligible to vote:", age1 >= 18 and age2 >= 18)
print("At least one eligible:", age1 >= 18 or age2 >= 18)
print("First person not eligible:", not(age1 >= 18))