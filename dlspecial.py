#this program will tell the total number of letters, digit and special character in an entere string
s = input("Enter a string: ")
digits = letters = special = 0

for ch in s:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        letters += 1
    else:
        special += 1

print("Letters:", letters)
print("Digits:", digits)
print("Special characters:", special)
