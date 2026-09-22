import math

x = float(input())
y = float(input())
z = float(input())
s = (x ** (y + 1) + math.exp(y - 1)) / (1 + x * abs(y - math.tan(z))) * (1 + abs(y - x)) + abs(y - x) ** 2 / 2 - abs(y - x) ** 3 / 3
print('{0:.6f}'.format(s))
