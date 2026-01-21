#this code will remove all the digits from a string
s = input("Enter string: ")
result = ""

for ch in s:
    if not ch.isdigit():
        result += ch

print(result)
"""
Enter string: Yasha@2305
output:
Yasha@
"""
