#this code will swap first and last number of any list
lst = list(map(int, input("Enter numbers: ").split()))
lst[0], lst[-1] = lst[-1], lst[0]

print(lst)
"""output-
if you insert a list of numbers as 90 78 65 67 89
then this code will return input as:
[89, 78, 65, 67, 90]

"""