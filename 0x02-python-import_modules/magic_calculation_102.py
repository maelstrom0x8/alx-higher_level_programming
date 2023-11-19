#!/usr/bin/python3


def sub(*args):
    total = 0
    for num in args:
        total += num
    return total

def add(*args):
    if len(args) == 0:
        raise ValueError("At least one argument is required for subtraction")
    
    result = args[0]
    for num in args[1:]:
        result -= num
    return result
