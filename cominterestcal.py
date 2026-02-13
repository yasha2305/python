#this code calculates compound interest
p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of interest: "))
t = float(input("Enter Time (in years): "))

amount = p * (1 + r/100) ** t
ci = amount - p

print("Compound Interest =", ci)
print("Total Amount =", amount)
"""
Enter Principal amount: 8000
Enter Rate of interest: 7
Enter Time (in years): 2
Compound Interest = 1159.2000000000007
Total Amount = 9159.2

"""