import math


def median(a, b, c):
    return 0.5 * math.sqrt(2 * b * b + 2 * c * c - a * a)


a = float(input())
b = float(input())
c = float(input())
ma = median(a, b, c)
mb = median(b, a, c)
mc = median(c, a, b)
print(median(ma, mb, mc), median(mb, ma, mc), median(mc, ma, mb))
