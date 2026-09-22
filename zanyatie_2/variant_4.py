import math

x = float(input())
y = float(input())
z = float(input())
s = abs(math.cos(x) - math.cos(y)) ** (1 + 2 * math.sin(y) ** 2) * (1 + z + z ** 2 / 2 + z ** 3 / 3 + z ** 4 / 4)
print('{0:.6f}'.format(s))
