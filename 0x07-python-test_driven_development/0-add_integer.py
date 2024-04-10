#!/usr/bin/python3
"""This is a "0_add_integer" module

The module supplies one function, add function

"""


def add_integer(a, b=98):
    if type(a) != integer and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != int:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
