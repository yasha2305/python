#this program will print the sum of natural numbers till the given range
n = int(input("Enter N: "))
total = 0

for i in range(1, n+1):
    total += i

print("Sum =", total)