import math


def hypotenuse(a, b):
    return math.sqrt(a * a + b * b)


c1 = hypotenuse(float(input()), float(input()))
c2 = hypotenuse(float(input()), float(input()))
if c1 > c2:
    print("Больше гипотенуза первого треугольника:", c1, "меньше второго:", c2)
elif c2 > c1:
    print("Больше гипотенуза второго треугольника:", c2, "меньше первого:", c1)
else:
    print("Гипотенузы равны:", c1)
