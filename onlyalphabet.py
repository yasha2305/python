#this program will tell you whether the entered string contains alphabets or it contains alphabets with digits with special characters
s = input("Enter string: ")

if s.isalpha():
    print("Only alphabets")
else:
    print("Contains other characters")
"""
example 1 -
Enter string : Yasha's age is 20 
output-
Contains other characters
"""
"""
example 2 -
Enter string : My name is yasha
output-
only alphabets
"""