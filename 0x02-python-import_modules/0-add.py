#!/usr/bin/python3
calc = __import__("add_0")

if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, calc.add(a, b)), end="\n")
