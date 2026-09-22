import math


def cbrt(v):
    return math.copysign(abs(v) ** (1 / 3), v)


x = float(input())
y = float(input())
z = float(input())
s = abs(x ** (y / x) - cbrt(y / x)) + (y - x) * (math.cos(y) - z / (y - x)) / (1 + (y - x) ** 2)
print('{0:.6f}'.format(s))
