def area(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Incorrect input: side lengths cannot be negative")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError(
            "Invalid triangle: the sum of any two sides must be greater than the third"
        )

    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def perimeter(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Incorrect input: side lengths cannot be negative")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError(
            "Invalid triangle: the sum of any two sides must be greater than the third"
        )

    return a + b + c
