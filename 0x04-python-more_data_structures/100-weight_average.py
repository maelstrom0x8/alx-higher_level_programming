#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    ts = 0
    tw = 0

    for score, weight in my_list:
        ts += score * weight
        tw += weight

    return (ts / tw)
