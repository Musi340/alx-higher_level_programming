#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1
    y = number % 10
    print(y, end="")
    return y
