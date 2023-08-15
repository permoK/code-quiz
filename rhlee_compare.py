#!/usr/bin/python3

def compare1(my_list=[]):

    if not my_list:
        pass

    length = len(my_list)

    if (my_list[0] == my_list[length - 1]):
        return (1)
    return (0)
