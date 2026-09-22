import math


def circle_area(r):
    return math.pi * r ** 2


def rectangle_area(a, b):
    return a * b


def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def square_area(a):
    return a * a


def trapezoid_area(a, b, h):
    return (a + b) / 2 * h


print("1 - круг, 2 - прямоугольник, 3 - треугольник, 4 - квадрат, 5 - трапеция")
choice = input()
if choice == "1":
    r = float(input("Радиус: "))
    print(circle_area(r))
elif choice == "2":
    a = float(input("Длина: "))
    b = float(input("Ширина: "))
    print(rectangle_area(a, b))
elif choice == "3":
    a = float(input("Сторона a: "))
    b = float(input("Сторона b: "))
    c = float(input("Сторона c: "))
    print(triangle_area(a, b, c))
elif choice == "4":
    a = float(input("Сторона: "))
    print(square_area(a))
elif choice == "5":
    a = float(input("Основание a: "))
    b = float(input("Основание b: "))
    h = float(input("Высота: "))
    print(trapezoid_area(a, b, h))
else:
    print("Нет такой фигуры")
