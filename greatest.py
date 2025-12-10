a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    print("Largest number =", a)
else:
    print("Largest number =", b)
if a > c:
    print("Largest number =",a)
else:
    print("Largest number =",c) 
    if b>c:
        print("Largest number =",b)
    else:
        print("Largest number =",c)