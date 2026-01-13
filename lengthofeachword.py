#this code will print length of each word of a sentence
s = input("Enter sentence: ")

for w in s.split():
    print(w, ":", len(w))
"""
Enter sentence: 
you are the best
output:
you : 3
are : 3
the : 3
best : 4
"""