#!/usr/bin/python3

import ctypes

my_lib = ctypes.CDLL("./libcheckpalindrome.so")
my_lib.check_palindrome.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
my_lib.check_palindrome.restype = ctypes.c_int

my_lib.to_string.argtypes = [ctypes.c_int]
my_lib.to_string.restype = ctypes.c_char_p


num = 1111

string = my_lib.to_string(num)

result = my_lib.check_palindrome(string, 0, len(string) - 1)

print (result)

#libc = ctypes.CDLL(None)
#libc.free(string)
