#!/usr/bin/python3
def pow(a, b):
    if b < 0:
        b *= -1
        k = a * pow(a, b - 1)
        return 1 / k
    elif b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * pow(a, b - 1)
