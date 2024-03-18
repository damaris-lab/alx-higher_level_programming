#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_no = my_list[0]
    for num in my_list:
        if num > max_no:
            max_no = num
        return (max_no)
