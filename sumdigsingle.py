n = input("Enter number: ")

while len(n) > 1:
    n = str(sum(int(d) for d in n))

print("Single digit:", n)
"""
Enter number: 29
output:
Single digit: 2
"""
