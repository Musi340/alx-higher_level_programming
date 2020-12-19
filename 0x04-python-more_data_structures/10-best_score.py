#!/usr/bin/python3
def best_score(a_dictionary):
    mymax = 0
    if not a_dictionary:
        return None
    for i in a_dictionary:
        if a_dictionary[i] > mymax:
            mymax = a_dictionary[i]
            myvalue = i
    return myvalue
