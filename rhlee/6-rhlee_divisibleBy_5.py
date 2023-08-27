#!/usr/bin/python3

if __name__ == "__main__":

    my_list = [10, 20, 33, 46, 55]

    length = len(my_list)

    print("given list is:", end="")

    for i in range(length - 1):
        print("{}".format(my_list[i]), end=", ")

    print("{}".format(my_list[length - 1]))
    print("those divisible by five are:")

    i = 0

    for i in range(length):
        if (my_list[i] % 5 == 0):
            print("{}".format(my_list[i]), end=", ")
    print()
