#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv
    import sys;
    from rhlee_compare import compare1

    listy = []
    length = len(argv)

    if (length == 1):
        print("No arguement given")
        sys.exit(1)

    for i in range(1, length):
        listy.append(argv[i])

    if (compare1(listy) == 1):
        print("true")
    else:
        print("false")

