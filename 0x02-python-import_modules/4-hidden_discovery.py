#!/usr/bin/python3
hidden = __import__("hidden_4")

if __name__ == "__main__":
    symbols = dir(hidden)
    symbols.sort()
    for obj in symbols:
        if not obj.startswith("__"):
            print("{}".format(obj), end="\n")
