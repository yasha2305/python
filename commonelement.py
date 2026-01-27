a = list(map(int, input("List 1: ").split()))
b = list(map(int, input("List 2: ").split()))

print(list(set(a) & set(b)))
"""
List 1: 80 90 100 1 3 4
List 2: 89 80 78 34 6 7
output:
[80]
"""