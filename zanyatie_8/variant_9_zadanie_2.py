def read_array():
    n = int(input())
    return [int(input()) for i in range(n)]


def print_info(a):
    product = 1
    for x in a:
        product *= x
    print("Произведение:", product, "Среднее:", sum(a) / len(a))


for k in range(3):
    array = read_array()
    print_info(array)
