def zadanie_1():
    n = int(input())
    a = [list(map(float, input().split())) for i in range(n)]
    k = int(input())
    d = a[k - 1][k - 1]
    if d == 0:
        print("Диагональный элемент равен нулю")
    else:
        for j in range(n):
            a[k - 1][j] = a[k - 1][j] / d
    for row in a:
        print(*row)


def zadanie_2():
    n = int(input())
    a = [list(map(int, input().split())) for i in range(n)]
    t = [[a[i][j] for i in range(n)] for j in range(n)]
    for row in t:
        print(*row)


tasks = {
    "1": zadanie_1,
    "2": zadanie_2,
}
number = input("Номер задания (1, 2): ").strip()
if number in tasks:
    tasks[number]()
else:
    print("Нет такого задания")
