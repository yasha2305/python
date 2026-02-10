lst = list(map(int, input("Enter numbers: ").split()))
lst = lst[1:] + lst[:1]

print(lst)
"""
Enter numbers: 67 87 113 76  53 201
output:
[87, 113, 76, 53, 201, 67]
"""