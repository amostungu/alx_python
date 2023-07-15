for i in range(99):
    print("{:2d} {:02X}".format(i, i), end=", " if i < 98 else "n")
