#!/usr/bin/python3
def fizzbuzz():
    for i in range(100):
        if 0 < i:
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz", end=" ")
            elif i % 3 == 0:
                print("Fizz", end=" ")
            elif i % 5 == 0:
                print("Buzz", end=" ")
            else:
                print("{:d}".format(i), end=" ")
    print("Buzz ", end="")
