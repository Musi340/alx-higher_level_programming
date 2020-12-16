#!/usr/bin/python3
def islower(c):
    i = 97
    while i < 123:
        if c == chr(i):
            return True
        i += 1
    return False
   #for k in "abcdefghijklmnpqrstuvwxyz":
        #if c == k:
           #return True
    #return False
