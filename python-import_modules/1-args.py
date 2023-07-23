#!/usr/bin/python3
if __name__ = "__main__":
    import sys
    for i in range(count):
        print("{}: {}".formart(i + 1, sys.argv[i + 1]))

    count = len(argv)-1
    if count == 0:
        print("0 argument:")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} argument:".format(count))
