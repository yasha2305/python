n = int(input("Enter length of binary string: "))
limit = int(input("Enter cost limit: "))

def generate(s, cost):
    if len(s) == n:
        print(s, "Cost =", cost)
        return

    # Add 0
    generate(s + "0", cost)

    # Add 1 only if cost stays within limit
    if cost + 1 <= limit:
        generate(s + "1", cost + 1)

generate("", 0)