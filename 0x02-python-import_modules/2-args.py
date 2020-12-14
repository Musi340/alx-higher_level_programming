#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("{:d} arguments.".format(len(argv) - 1))
    elif len(argv) > 1:
        if len(argv) == 2:
            print("{:d} argument:".format(len(argv) - 1))
        elif len(argv) > 2:
            print("{:d} arguments:".format(len(argv) - 1))
        for i in range(len(argv)):
            if i > 0:
                print("{:d}: {:s}".format(i, argv[i]))
                i += 1
