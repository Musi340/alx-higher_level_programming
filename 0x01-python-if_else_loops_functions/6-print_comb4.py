#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        for k in range(10):
            if i != j and i != k and j != k:
                if i < j and j < k:
                    if i != 7 and i != 8 and j != 9:
                        print("{0:d}{1:d}{2:d}".format(i ,j ,k), end=", ")
                    else:
                        print("{0:d}{1:d}{2:d}".format(i ,j ,k))      
