#!/usr/bin/python3

def no_c(my_string: str):
    res = ""
    for s in my_string:
        if 'c' in s or 'C' in s:
            pass
        else:
            res += s
    return (res)
