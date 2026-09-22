def read_array():
    n = int(input())
    return [int(input()) for i in range(n)]


def print_info(a):
    total = sum(a)
    print("Сумма:", total, "Среднее:", total / len(a))


for k in range(3):
    array = read_array()
    print_info(array)
