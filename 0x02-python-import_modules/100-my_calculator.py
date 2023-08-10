#!/usr/bin/python3
import sys
calc = __import__("calculator_1")

if __name__ == "__main__":
    argc = len(sys.argv)
    operators = "/*-+"
    if argc < 4:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"),
              end="\n")
        sys.exit(1)
    if sys.argv[2] not in operators:
        print("{}"
              .format("Unknown operator. Available operators: +, -, * and /"),
              end="\n")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    result = None

    if operator == "+":
        result = calc.add(a, b)
    elif operator == "-":
        result = calc.sub(a, b)
    elif operator == "*":
        result = calc.mul(a, b)
    elif operator == "/":
        if b != 0:
            result = calc.div(a, b)
        else:
            print("{}".format("Division by zero is not allowed"), end="\n")
            sys.exit(1)

    print("{} {} {} = {}".format(a, operator, b, result), end="\n")
