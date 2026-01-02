#this program will print the smallest word in a sentence
sentence = input("Enter sentence: ")
words = sentence.split()

print("Smallest word:", min(words, key=len))
