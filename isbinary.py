#this code will tell you that the entered digit is binary or not 
n = input("Enter number: ")

if all(ch in '01' for ch in n):
    print("Binary number")
else:
    print("Not binary")
