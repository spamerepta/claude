import math


def cbrt(v):
    return math.copysign(abs(v) ** (1 / 3), v)


x = float(input())
y = float(input())
z = float(input())
s = y ** cbrt(abs(x)) + math.cos(y) ** 3 * abs(x - y) * (1 + math.sin(z) ** 2 / math.sqrt(x + y)) / (math.exp(abs(x - y)) + x / 2)
print('{0:.6f}'.format(s))
