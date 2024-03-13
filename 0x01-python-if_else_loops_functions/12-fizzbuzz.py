#!/usr/bin/env python3
def fizzbuzz():
    for i in range(1, 100):
        if i % 3 == 0:
            print('fizz', end="")
        elif i % 5 == 0:
            print('buzz', end="")
        elif i % 15 == 0:
            print('fizbuzz', end="")
        else:
            print(f'{:d}'.format(i), end="")
