import math


def cbrt(v):
    return math.copysign(abs(v) ** (1 / 3), v)


x = float(input())
y = float(input())
z = float(input())
s = (y + cbrt(x - 1)) ** (1 / 4) / (abs(x - y) * (math.sin(z) ** 2 + math.tan(z)))
print('{0:.6f}'.format(s))
