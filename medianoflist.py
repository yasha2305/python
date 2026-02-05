lst = sorted(list(map(int, input("Enter numbers: ").split())))
n = len(lst)

if n % 2 == 0:
    print("Median:", (lst[n//2 - 1] + lst[n//2]) / 2)
else:
    print("Median:", lst[n//2])
"""
Enter numbers: 4 5 67 8 6 59
output:
Median: 7.0
"""