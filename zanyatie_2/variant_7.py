import math

x = float(input())
y = float(input())
z = float(input())
s = 5 * math.atan(x) - 1 / 4 * math.acos(x) * (x + 3 * abs(x - y) + x ** 2) / (abs(x - y) * z + x ** 2)
print('{0:.6f}'.format(s))
