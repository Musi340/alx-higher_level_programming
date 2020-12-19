#!/usr/bin/python3
def weight_average(my_list=[]):
    mysum = 0
    myavg = 0
    if not my_list:
        return 0
    for i in my_list:
        myprod = i[0] * i[1]
        mysum += myprod
        myavg += i[1]
    return mysum/myavg
