#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mylist = []
    k = []
    for i in range(len(matrix)):
        k = list(map(lambda x: x*x, matrix[i]))
        mylist = mylist + [k]
    return mylist       
