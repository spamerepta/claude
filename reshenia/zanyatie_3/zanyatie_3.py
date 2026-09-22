def zadanie_1():
    a = int(input())
    b = int(input())
    c = int(input())
    print(a + b + c)


def zadanie_2():
    a = float(input())
    b = float(input())
    print(a * b / 2)


def zadanie_3():
    n = int(input())
    n = n % (24 * 60)
    print(n // 60, n % 60)


def zadanie_4():
    def lace_length(a, b, l, n):
        return 2 * l + (2 * n - 1) * a + 2 * (n - 1) * b

    a = int(input())
    b = int(input())
    l = int(input())
    n = int(input())
    print(lace_length(a, b, l, n))


def zadanie_5():
    def print_min(a, b, c):
        smallest = a
        if b < smallest:
            smallest = b
        if c < smallest:
            smallest = c
        print(smallest)

    a = int(input())
    b = int(input())
    c = int(input())
    print_min(a, b, c)


def zadanie_6():
    def same_color(x1, y1, x2, y2):
        if (x1 + y1) % 2 == (x2 + y2) % 2:
            print("Да")
        else:
            print("Нет")

    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    same_color(x1, y1, x2, y2)


def zadanie_7():
    def is_leap(year):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print("Да")
        else:
            print("Нет")

    year = int(input())
    is_leap(year)


def zadanie_8():
    def count_equal(a, b, c):
        if a == b == c:
            print(3)
        elif a == b or b == c or a == c:
            print(2)
        else:
            print(0)

    a = int(input())
    b = int(input())
    c = int(input())
    count_equal(a, b, c)


def zadanie_9():
    def can_break(n, m, k):
        if k < n * m and (k % n == 0 or k % m == 0):
            print("Да")
        else:
            print("Нет")

    n = int(input())
    m = int(input())
    k = int(input())
    can_break(n, m, k)


def dop_zadanie():
    a = int(input())
    b = int(input())
    c = int(input())
    for number in (a, b, c):
        if 1 <= number <= 3:
            print(number)


tasks = {
    "1": zadanie_1,
    "2": zadanie_2,
    "3": zadanie_3,
    "4": zadanie_4,
    "5": zadanie_5,
    "6": zadanie_6,
    "7": zadanie_7,
    "8": zadanie_8,
    "9": zadanie_9,
    "dop": dop_zadanie,
}
number = input("Номер задания (1, 2, 3, 4, 5, 6, 7, 8, 9, dop): ").strip()
if number in tasks:
    tasks[number]()
else:
    print("Нет такого задания")
