def zadanie_1():
    a = int(input())
    b = int(input())
    for i in range(a, b + 1):
        print(i)


def zadanie_2():
    a = int(input())
    b = int(input())
    if a < b:
        for i in range(a, b + 1):
            print(i)
    else:
        for i in range(a, b - 1, -1):
            print(i)


def zadanie_3():
    a = int(input())
    b = int(input())
    for i in range(a, b - 1, -1):
        if i % 2 != 0:
            print(i)


def zadanie_4():
    total = 0
    for i in range(int(input())):
        total += int(input())
    print(total)


def zadanie_5():
    n = int(input())
    total = 0
    for i in range(1, n + 1):
        total += i ** 3
    print(total)


def zadanie_6():
    n = int(input())
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(factorial)


def zadanie_7():
    n = int(input())
    factorial = 1
    total = 0
    for i in range(1, n + 1):
        factorial *= i
        total += factorial
    print(total)


def zadanie_8():
    n = int(input())
    for i in range(1, n + 1):
        step = ""
        for j in range(1, i + 1):
            step += str(j)
        print(step)


def zadanie_9():
    n = int(input())
    a, b = 1, 1
    total = 0
    for i in range(n):
        total += a
        a, b = b, a + b
    print(total)


def zadanie_10():
    n = int(input())
    k = int(input())
    a, b = 1, 1
    total = 0
    for i in range(1, k + n):
        if i >= k:
            total += a
        a, b = b, a + b
    print(total)


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
    "10": zadanie_10,
}
number = input("Номер задания (1, 2, 3, 4, 5, 6, 7, 8, 9, 10): ").strip()
if number in tasks:
    tasks[number]()
else:
    print("Нет такого задания")
