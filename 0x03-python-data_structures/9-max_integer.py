#!/usr/bin/python3
def max_integer(my_list=[]):

    if len(my_list) == 0:
        return( None)
    
    max_no = my_list[0]
    for num in range(len(my_list)):
        if num > max_no:
            max_no = num
        return (max_no)
