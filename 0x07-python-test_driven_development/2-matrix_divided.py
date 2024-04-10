#!/usr/bin/python3
"""This module provides a function that divides all elements of a matrix
"""

def matrix_divided(matrix, div):
    """
    divides all elements of a matrix

    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not instance(div, (int, float)):
        raise TypeError("div must be a number")
    if not all(instance(row, list) and 
            all(instance(num, (int, float))
