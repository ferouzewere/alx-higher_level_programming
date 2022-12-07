#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = ""

if number >= 0:
    last = int(repr(number)[-1])
else:
    last = int(repr(number)[-1]) * (-1)

if last > 5:
    string = "and is greater than 5"
elif last == 0:
    string = "and is 0"
elif last < 6 and last != 0:
    string = "and is less than 6 and not 0"
else:
    pass

print("Last digit of {} is {} {}".format(number, last, string))
