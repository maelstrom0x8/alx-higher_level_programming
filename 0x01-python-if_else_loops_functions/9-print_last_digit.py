#!/usr/bin/python3
def print_last_digit(number):
    last_digit = ('{}'.format(number))
    last_digit = int(last_digit[-1])
    print(last_digit, end='')
    return last_digit
