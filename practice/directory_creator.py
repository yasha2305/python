import os

name = input("Folder Name: ")

os.makedirs(name, exist_ok=True)

print("Folder Created")