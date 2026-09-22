def zadanie_1():
    def divisible_by_digits(number):
        x = number
        while x > 0:
            digit = x % 10
            if digit == 0 or number % digit != 0:
                return False
            x //= 10
        return True

    n = int(input())
    result = []
    for i in range(1, n + 1):
        if divisible_by_digits(i):
            result.append(i)
    print(*result)


def zadanie_2():
    def swap_first_last(a):
        a[0], a[-1] = a[-1], a[0]

    m = int(input())
    a = [int(input()) for i in range(m)]
    print(a)
    swap_first_last(a)
    print(a)


tasks = {
    "1": zadanie_1,
    "2": zadanie_2,
}
number = input("Номер задания (1, 2): ").strip()
if number in tasks:
    tasks[number]()
else:
    print("Нет такого задания")
