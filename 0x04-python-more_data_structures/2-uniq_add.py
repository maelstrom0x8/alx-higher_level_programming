#!/usr/bin/python3

def uniq_add(my_list=[]):
    nlist = []
    sum = 0
    for i in my_list:
        if i not in nlist:
            sum = sum + i
            nlist.append(i)
    return (sum)
