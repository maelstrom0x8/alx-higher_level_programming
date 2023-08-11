#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list_cpy = my_list[:]
    if 0 > idx or idx > len(list_cpy) - 1:
        return (list_cpy)
    else:
        list_cpy[idx] = element
        return (list_cpy)
