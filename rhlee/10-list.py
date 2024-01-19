#!/usr/bin/python3

import ctypes

my_lib = ctypes.CDLL("./libPyList.so")
my_lib.print_python_list_info.argtypes = [ctypes.py_object]


my_list =["Hello", 2]

my_lib.print_python_list_info(my_list)
