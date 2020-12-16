#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j and i != j:
            print("{0:d}{1:d}".format(i, j))
           
