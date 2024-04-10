#!/usr/bin/python3
"""
this module contains function print square
"""


def print_square(size):
    """print_square: prints square to stdout"""
    if not instance(size, int):
        raise TypeError("size must be an integer")
    elif not instance(size, int) and size < 0:
        raise TypeError("size mmust be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j i range(size):
            if i + 1 == size:
                print('#')
            else:
                print('#', end="")
