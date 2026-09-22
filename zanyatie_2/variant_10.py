import math


def cbrt(v):
    return math.copysign(abs(v) ** (1 / 3), v)


x = float(input())
y = float(input())
z = float(input())
s = 2 ** -x * math.sqrt(x + abs(y) ** (1 / 4)) * cbrt(math.exp(x - 1 / math.sin(z)))
print('{0:.6f}'.format(s))
