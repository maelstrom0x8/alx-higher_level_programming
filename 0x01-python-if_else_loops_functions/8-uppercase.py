#!/usr/bin/python3
def uppercase(str):
    s = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            s += (chr(ord(char) - ord('a') + ord('A')))
        else:
            s += char
    print("{}".format(s))
