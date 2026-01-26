lst = input("Enter elements (use space): ").split(" ")

lst = [i for i in lst if i != ""]
print(lst)
"""
Enter elements (use space): yasha = success
output:
['yasha', '=', 'success']
"""
