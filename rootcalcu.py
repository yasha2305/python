n = input("Enter number: ")

while len(n) > 1:
    n = str(sum(int(d) for d in n))

print("Digital Root:", n)
"""
Enter number: 78
output:
Digital Root: 6
"""