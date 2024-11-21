import math


def area(r):
    if r < 0:
        print("incorrect input")
        exit(-1)
    return math.pi * r * r


def perimeter(r):
    if r < 0:
        print("incorrect input")
        exit(-1)
    return 2 * math.pi * r
