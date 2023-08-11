#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argc = len(sys.argv)
    if argc < 2:
        print("{} arguments".format(0), end="\n")
    elif argc == 2:
        print("{} argument".format(1), end="\n")
        print("{}: {}".format(1, sys.argv[1]))
    elif argc > 2:
        print("{} arguments".format(argc - 1), end="\n")
        for i in range(1, argc):
            print("{}: {}".format(i, sys.argv[i]), end="\n")
