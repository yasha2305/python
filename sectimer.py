#this code is for a timer one can input any number can the code will give output as countdown and when the time is over i.e, the countdown is complete the output will be print as Time's up!
import time

n = int(input("Enter seconds: "))
while n > 0:
    print(n)
    time.sleep(1)
    n -= 1
print("Time's up!")
