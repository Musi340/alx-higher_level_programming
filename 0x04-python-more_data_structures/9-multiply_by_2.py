#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mydict = {}
    for i in a_dictionary:
        value = a_dictionary[i]*2
        mydict[i] = value
    return mydict
