#!/usr/bin/python3
calculator = __import__('calculator_1')

if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, calculator.add(a, b)), end="\n")
    print("{} - {} = {}".format(a, b, calculator.sub(a, b)), end="\n")
    print("{} * {} = {}".format(a, b, calculator.mul(a, b)), end="\n")
    print("{} / {} = {}".format(a, b, calculator.div(a, b)), end="\n")
