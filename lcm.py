#LCM
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

max = a if a > b else b

while True:
    if max % a == 0 and max % b == 0:
        print("LCM is:", max)
        break
    max += 1
