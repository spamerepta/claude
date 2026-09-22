def zadanie_1():
    print("Курс Основы программирования начался")


def zadanie_2():
    print(16823 * 12302 % 3092)


def zadanie_3():
    age = int(input())
    if age >= 16:
        print("Поздравляем вы поступили в ВГУИТ")
    else:
        print("Сначала нужно окончить школу!")


def zadanie_3_1():
    age = int(input())
    if age <= 0 or age >= 75:
        print("Некорректный возраст")
    elif age >= 16:
        print("Поздравляем вы поступили в ВГУИТ")
    else:
        print("Сначала нужно окончить школу!")


def zadanie_3_2():
    name = input()
    age = int(input())
    if name == "Иван":
        print("Иван не может поступить")
    elif age <= 0 or age >= 75:
        print("Некорректный возраст")
    elif age >= 16:
        print("Поздравляем вы поступили в ВГУИТ")
    else:
        print("Сначала нужно окончить школу!")


def zadanie_3_3():
    name = input()
    age = int(input())
    if name == "Иван":
        print("Иван не может поступить")
    elif age <= 0 or age >= 75:
        print("Некорректный возраст")
    elif age >= 16:
        print("Поздравляем вы поступили в ВГУИТ")
    else:
        print("Сначала нужно окончить школу!")
        print("Осталось учиться в школе:", 16 - age)


def zadanie_4():
    seconds = int(input())
    days = seconds // 86400
    hours = seconds % 86400 // 3600
    minutes = seconds % 3600 // 60
    secs = seconds % 60
    print(str(days) + ":" + str(hours) + ":" + str(minutes) + ":" + str(secs))


def zadanie_5():
    n = input()
    n = int(n)
    print(n + n ** 2 + n ** 3 + n ** 4 + n ** 5)


def zadanie_6():
    x = input()
    y = input()
    x, y = y, x
    print(x, y)


def zadanie_7():
    number = int(input())
    if number % 2 == 0:
        print("Число четное")
    else:
        print("Число нечетное")


def dop_zadanie():
    name = input("Ваши фамилия, имя? ")
    age = input("Сколько Вам лет? ")
    city = input("Где вы живете? ")
    print("Ваши фамилия, имя:", name)
    print("Ваш возраст:", age)
    print("Вы живете в", city)


tasks = {
    "1": zadanie_1,
    "2": zadanie_2,
    "3": zadanie_3,
    "3.1": zadanie_3_1,
    "3.2": zadanie_3_2,
    "3.3": zadanie_3_3,
    "4": zadanie_4,
    "5": zadanie_5,
    "6": zadanie_6,
    "7": zadanie_7,
    "dop": dop_zadanie,
}
number = input("Номер задания (1, 2, 3, 3.1, 3.2, 3.3, 4, 5, 6, 7, dop): ").strip()
if number in tasks:
    tasks[number]()
else:
    print("Нет такого задания")
