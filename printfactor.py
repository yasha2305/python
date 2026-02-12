n = int(input("Enter number: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
"""
Enter number: 56
output:
1 2 4 7 8 14 28 56 
"""