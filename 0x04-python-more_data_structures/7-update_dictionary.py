#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    k = 0
    for i in a_dictionary:
        if i == key:
            k += 1
    if k == 0:
        a_dictionary[key] = value
    if k > 0:
        for i in a_dictionary:
            if i == key:
                a_dictionary[i] = value
    return a_dictionary
        
        
