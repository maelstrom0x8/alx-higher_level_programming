#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    res = {}
    for k, v in a_dictionary.items():
        res.update({k: (v * 2)})
    return (res)
