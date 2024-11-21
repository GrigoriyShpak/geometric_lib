def area(a, b, c):
    if a < 0 or b < 0 or c < 0:
        print("incorrect input")
        exit(-1)
    return (a + b + c) / 2


def perimeter(a, b, c):
    if a < 0 or b < 0 or c < 0:
        print("incorrect input")
        exit(-1)
    return a + b + c
