#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    mylist = list(set(my_list))
    for i in mylist:
        sum += i
    return sum
