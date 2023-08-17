#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    Ks = list(a_dictionary.keys())
    Ks.sort()
    for sk in Ks:
        print("{}: {}".format(sk, a_dictionary[sk]))
