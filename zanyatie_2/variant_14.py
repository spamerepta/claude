import math


def cbrt(v):
    return math.copysign(abs(v) ** (1 / 3), v)


x = float(input())
y = float(input())
z = float(input())
s = y ** (x + 1) / (cbrt(abs(y - 2)) + 3) + (x + y / 2) / (2 * abs(x + y)) * (x + 1) ** (-1 / math.sin(z))
print('{0:.6f}'.format(s))
