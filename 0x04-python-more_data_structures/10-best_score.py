#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is not None:
        keys = list(a_dictionary.keys())
        max, top = 0, ""

        for k in keys:
            if a_dictionary[k] > max:
                max = a_dictionary[k]
                top = k
        return (top)
