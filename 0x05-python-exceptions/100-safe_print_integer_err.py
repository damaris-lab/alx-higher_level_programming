#!/usr/bin/python3
import sys


def safe_print_integer_err(value):

    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as V:
        sys.stderr.write("Exception: " + V.args[0] + "\n")
        return False
