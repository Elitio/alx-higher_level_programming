#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_int = number % 10

if l_int > 5:
    print(f"Last digit of {number:d} is {l_int} and is greater than 5")
elif l_int == 0:
    print(f"Last digit of {number:d} is {l_int} and is 0")
elif last_int > 0 and last_digit < 6:
    print(f"Last digit of {number:d} is {l_int} and is less than 6 and not 0")
