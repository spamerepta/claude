def zadanie_1():
    n = int(input())
    i = 1
    while i * i <= n:
        print(i * i)
        i += 1


def zadanie_2():
    n = int(input())
    d = 2
    while n % d != 0:
        d += 1
    print(d)


def zadanie_3():
    n = int(input())
    power = 0
    value = 1
    while value * 2 <= n:
        value *= 2
        power += 1
    print(power, value)


def zadanie_4():
    x = float(input())
    y = float(input())
    day = 1
    while x < y:
        x *= 1.1
        day += 1
    print(day)


def zadanie_5():
    count = 0
    number = int(input())
    while number != 0:
        count += 1
        number = int(input())
    print(count)


def zadanie_6():
    count = 0
    total = 0
    number = int(input())
    while number != 0:
        count += 1
        total += number
        number = int(input())
    print(total / count)


def zadanie_7():
    previous = int(input())
    count = 0
    if previous != 0:
        number = int(input())
        while number != 0:
            if number > previous:
                count += 1
            previous = number
            number = int(input())
    print(count)


def zadanie_8():
    previous = int(input())
    current_length = 1
    max_length = 1
    number = int(input()) if previous != 0 else 0
    while number != 0:
        if number == previous:
            current_length += 1
        else:
            current_length = 1
        if current_length > max_length:
            max_length = current_length
        previous = number
        number = int(input())
    print(max_length)


tasks = {
    "1": zadanie_1,
    "2": zadanie_2,
    "3": zadanie_3,
    "4": zadanie_4,
    "5": zadanie_5,
    "6": zadanie_6,
    "7": zadanie_7,
    "8": zadanie_8,
}
number = input("Номер задания (1, 2, 3, 4, 5, 6, 7, 8): ").strip()
if number in tasks:
    tasks[number]()
else:
    print("Нет такого задания")
