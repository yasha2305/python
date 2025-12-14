#this program will print total prime numbers in an given number
n = int(input("Enter N: "))
count = 0

for num in range(2, n + 1):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        count += 1

print("Total prime numbers:", count)
