import math


def cbrt(v):
    return math.copysign(abs(v) ** (1 / 3), v)


x = float(input())
y = float(input())
z = float(input())
s = cbrt(9 + (x - y) ** 2) / (x ** 2 + y ** 2 + 2) - math.exp(abs(x - y)) * math.tan(z) ** 3
print('{0:.6f}'.format(s))
