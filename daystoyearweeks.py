#this code will convert days into years,weeks,days
days = int(input("Enter days: "))

years = days // 365
weeks = (days % 365) // 7
remaining_days = days % 7

print("Years:", years)
print("Weeks:", weeks)
print("Days:", remaining_days)
