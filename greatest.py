#This program will tell the greatest among three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Largest number =", a)
elif b > c: 
    print("Largest number =",b)
else:
    print("Largest number =",c)