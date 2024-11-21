def area(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Incorrect input: side lengths cannot be negative")
    return (a + b + c) / 2


def perimeter(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Incorrect input: side lengths cannot be negative")
    return a + b + c
