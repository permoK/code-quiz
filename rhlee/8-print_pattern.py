#!/usr/bin/python3

import ctypes

my_lib = ctypes.CDLL("./libprintpattern.so")

my_lib.print_pattern()
