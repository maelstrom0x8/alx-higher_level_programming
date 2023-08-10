#!/usr/bin/python3
add = __import__("add_0").add

if __name__ == "__main__":
    a = 1
    b = 2
    sum = add(a, b)
    print("{} + {} = {}".format(a, b, sum), end="\n")
