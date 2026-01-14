#This program takes a string input, converts it into a set to remove duplicate characters, and prints each unique character
s = input("Enter string: ")

for ch in set(s):
    print(ch, end=" ")
