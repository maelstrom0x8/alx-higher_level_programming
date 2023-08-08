#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_s =  ('{}'.format(number))
last = int(last_s[-1])
if last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif last == 0:
    print(f"Last digit of {number} is {last} and is 0")
elif last < 6 and last != 0:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
