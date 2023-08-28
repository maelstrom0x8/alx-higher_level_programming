#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    total = 0
    end = x
    for i in range(end):
        try:
            print("{:d}".format(my_list[i]), end="")
            total = total + 1
        except (ValueError, TypeError):
            continue
    print("")
    return (total)
