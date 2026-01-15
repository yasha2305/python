#This code Prints all numbers between 1 and N that are divisible by 5
n = int(input("Enter N: "))

for i in range(1, n + 1):
    if i % 5 == 0:
        print(i, end=" ") 