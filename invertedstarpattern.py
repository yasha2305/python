#this code will print the interverted star pattern for the entered number of rows
n = int(input("Enter rows: "))

for i in range(n, 0, -1):
    print("*" * i)
