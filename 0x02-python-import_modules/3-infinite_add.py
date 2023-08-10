#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum = 0
    if len(sys.argv) > 1:
        for e in sys.argv:
            try:
                sum += int(e)
            except ValueError:
                pass
    print("{}".format(sum), end="\n")
