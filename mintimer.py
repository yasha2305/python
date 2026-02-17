import time

m = int(input("Enter minutes: "))
seconds = m * 60

while seconds > 0:
    print(seconds)
    time.sleep(1)
    seconds -= 1

print("Time's up!")
"""
This program takes minutes as input, converts them into seconds, then counts down every second using a loop and time.sleep(1) until it reaches 0, and finally prints "Time's up!".

"""