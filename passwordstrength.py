#this code checks whether the password is strong or medium
password = input("Enter password: ")

if len(password) < 6:
    print("Weak password")
elif any(char.isdigit() for char in password) and any(char.isupper() for char in password):
    print("Strong password")
else:
    print("Medium password")
