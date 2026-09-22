import math


def right_triangle_area(a, b):
    return a * b / 2


def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


x = float(input())
y = float(input())
z = float(input())
t = float(input())
diagonal = math.sqrt(x * x + y * y)
print(right_triangle_area(x, y) + triangle_area(z, t, diagonal))
