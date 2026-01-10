# this is a code like counting items by pointing at each one and saying "1... 2... 3..." until you've pointed at everything in the box.
d = {"a": 1, "b": 2, "c": 3}
count = 0

for _ in d:
    count += 1

print("Length:", count)
