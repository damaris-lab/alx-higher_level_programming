#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    lst = list(a_dictionary)
    cpy_dict = a_dictionary.copy()

    for item in lst:
        cpy_dict[item] = cpy_dict[item] * 2
    return (cpy_dict)
