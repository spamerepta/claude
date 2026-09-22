import math


def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


a = float(input())
print(6 * triangle_area(a, a, a))
