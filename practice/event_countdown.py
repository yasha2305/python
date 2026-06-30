from datetime import datetime

date = input("Event Date (YYYY-MM-DD): ")

event = datetime.strptime(date, "%Y-%m-%d")

today = datetime.now()

days = (event - today).days

print("Days Left:", days)