#!/usr/bin/python3
def islower(c):
    if !(isinstance(c, str)):
        return False
    i = 97
    while i < 123:
        if c == chr(i):
            return True
        i += 1
    return False
