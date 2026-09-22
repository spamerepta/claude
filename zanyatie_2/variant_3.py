import math

x = float(input())
y = float(input())
z = float(input())
s = (1 + math.sin(x + y) ** 2) / abs(x - 2 * y / (1 + x ** 2 * y ** 2)) * x ** abs(y) + math.cos(math.atan(1 / z)) ** 2
print('{0:.6f}'.format(s))
