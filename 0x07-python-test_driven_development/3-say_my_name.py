#!/usr/bin/python3
"""
function that prints my name is <firtname><lastname>
"""


def say_my_name(first_name, last_name=""):
    """function to print names"""
    if type(first_name) != string:
        raise TypeError("first_name must be a string")
    if type(last_name) != string:
        raise TypeError("last_name must be a string")
    print(f"my name is {first_name} {last_name}")
