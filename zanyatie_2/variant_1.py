import math

x = float(input())
y = float(input())
z = float(input())
s = 2 * math.cos(x - 2 / 3) / (1 / 2 + math.sin(y) ** 2) * (1 + z ** 2 / (3 - z ** 2 / 5))
print('{0:.6f}'.format(s))
