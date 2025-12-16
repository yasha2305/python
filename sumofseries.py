#this program will print the sum of series
n = int(input("Enter terms: "))
num = 0
sum = 0

for i in range(n):
    num = num * 10 + 1
    sum += num

print("Sum of series:", sum)
""" give any input let suppose 5 then it will print the output as = 12345"""