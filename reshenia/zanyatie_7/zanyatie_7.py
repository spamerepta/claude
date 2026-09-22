def zadanie_1():
    n = int(input())
    a = [int(input()) for i in range(n)]
    product = 1
    for x in a:
        product *= x
    print("Сумма:", sum(a))
    print("Произведение:", product)


def zadanie_2():
    n = int(input())
    a = [float(input()) for i in range(n)]
    average = sum(a) / n
    for i in range(n):
        if a[i] == 0:
            a[i] = average
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
