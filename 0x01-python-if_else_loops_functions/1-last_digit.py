#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
value = number
if value < 0:
    value *= -1
k = value % 10
if k < 6 and k != 0:
    print("Last digit of {:} is {:} ".format(number, k), end="")
    print("and is less than 6 and not 0")
if k > 5:
    print("Last digit of {:} is {:} and is greater than 5".format(number, k))
if k == 0:
    print("Last digit of {:} is {:} and is 0".format(number, k))
