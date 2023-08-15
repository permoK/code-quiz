#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    import sys

    length = len(argv) - 1

    if (length != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    sign = argv[2]

    if sign not in ('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)


    a = int(argv[1])
    b = int(argv[3])

    if (sign == '+'):
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif (sign == '-'):
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif (sign == '*'):
        print("{} * {} = {}".format(a, b, mul(a * b)))
    else:
        print("{} /  {} = {}".format(a, b, div(a, b)))
