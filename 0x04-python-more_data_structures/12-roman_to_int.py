#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str:
        return 0
    if not roman_string:
        return 0
    mylist1 = [1, 5, 10, 50, 100, 500]
    mylist2 = ['I', 'V', 'X', 'L', 'C', 'D']
    mylist3 = []
    mysum = 0
    for i in roman_string:
        for k in range(len(mylist2)):
            if i == mylist2[k]:
                mylist3.append(mylist1[k])
    for m in range(len(mylist3) - 1):
        if mylist3[m] < mylist3[m + 1]:
            mysum += (mylist3[m]*-1)
        else:
            mysum += mylist3[m]
    mysum += mylist3[len(mylist3) - 1]
    return mysum
