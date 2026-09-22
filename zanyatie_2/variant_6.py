import math


def cbrt(v):
    return math.copysign(abs(v) ** (1 / 3), v)


x = float(input())
y = float(input())
z = float(input())
s = math.sqrt(10 * (cbrt(x) + x ** (y + 2))) * (math.asin(z) ** 2 - abs(x - y))
print('{0:.6f}'.format(s))
