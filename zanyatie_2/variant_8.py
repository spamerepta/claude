import math


def cbrt(v):
    return math.copysign(abs(v) ** (1 / 3), v)


x = float(input())
y = float(input())
z = float(input())
s = math.exp(abs(x - y)) * abs(x - y) ** (x + y) / (math.atan(x) + math.atan(z)) + cbrt(x ** 6 + math.log(y) ** 2)
print('{0:.6f}'.format(s))
