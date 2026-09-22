import math

x = float(input())
y = float(input())
z = float(input())
s = math.log(y ** -math.sqrt(abs(x))) * (x - y / 2) + math.sin(math.atan(z)) ** 2
print('{0:.6f}'.format(s))
