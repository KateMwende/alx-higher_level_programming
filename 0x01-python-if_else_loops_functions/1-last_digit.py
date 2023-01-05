#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    l_d = number % 10
elif number < 0:
    l_d = ((number * -1) % 10) * -1

if l_d > 5:
    str = f'Last digit of {number} is {l_d} and is greater than 5'
elif l_d < 6 and l_d != 0:
    str = f'Last digit of {number} is {l_d} and is less than 6 and not 0'
elif l_d == 0:
    str = f'Last digit of {number} is {l_d} and is 0'

print(str)
