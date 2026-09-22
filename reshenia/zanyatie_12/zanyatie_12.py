import sys


def blok_a_zadanie_1():
    def power_div_factorial(x, n):
        if n == 0:
            return 1
        return power_div_factorial(x, n - 1) * x / n

    x = int(input())
    n = int(input())
    print(power_div_factorial(x, n))


def blok_a_zadanie_2():
    def remainder(a, b):
        if a < b:
            return a
        return remainder(a - b, b)

    a = int(input())
    b = int(input())
    print(remainder(a, b))


def blok_a_zadanie_3():
    def reverse(n, result=0):
        if n == 0:
            return result
        return reverse(n // 10, result * 10 + n % 10)

    print(reverse(int(input())))


def blok_a_zadanie_4():
    def digit_sum(n):
        if n < 10:
            return n
        return n % 10 + digit_sum(n // 10)

    print(digit_sum(int(input())))


def blok_a_zadanie_5():
    def print_digits(n):
        print(n % 10, end=" ")
        if n >= 10:
            print_digits(n // 10)

    print_digits(int(input()))
    print()


def blok_a_zadanie_6():
    sys.setrecursionlimit(100000)

    def is_prime(n, d=2):
        if d * d > n:
            return True
        if n % d == 0:
            return False
        return is_prime(n, d + 1)

    n = int(input())
    if is_prime(n):
        print("YES")
    else:
        print("NO")


def blok_a_zadanie_7():
    def print_range(a, b):
        print(a)
        if a < b:
            print_range(a + 1, b)
        elif a > b:
            print_range(a - 1, b)

    a = int(input())
    b = int(input())
    print_range(a, b)


def blok_b_zadanie_1():
    def sequence_max():
        n = int(input())
        if n == 0:
            return 0
        rest = sequence_max()
        if n > rest:
            return n
        return rest

    print(sequence_max())


def blok_b_zadanie_2():
    def two_largest():
        n = int(input())
        if n == 0:
            return 0, 0
        first, second = two_largest()
        if n > first:
            return n, first
        if n > second:
            return first, n
        return first, second

    first, second = two_largest()
    print(second)


def blok_b_zadanie_3():
    def print_odd_positions():
        n = int(input())
        if n == 0:
            return
        print(n)
        n = int(input())
        if n == 0:
            return
        print_odd_positions()

    print_odd_positions()


def blok_b_zadanie_4():
    sys.setrecursionlimit(100000)

    def is_prime(n, d=3):
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        if d * d > n:
            return True
        if n % d == 0:
            return False
        return is_prime(n, d + 2)

    n = int(input())
    if is_prime(n):
        print("YES")
    else:
        print("NO")


tasks = {
    "A1": blok_a_zadanie_1,
    "A2": blok_a_zadanie_2,
    "A3": blok_a_zadanie_3,
    "A4": blok_a_zadanie_4,
    "A5": blok_a_zadanie_5,
    "A6": blok_a_zadanie_6,
    "A7": blok_a_zadanie_7,
    "B1": blok_b_zadanie_1,
    "B2": blok_b_zadanie_2,
    "B3": blok_b_zadanie_3,
    "B4": blok_b_zadanie_4,
}
number = input("Номер задания (A1, A2, A3, A4, A5, A6, A7, B1, B2, B3, B4): ").strip().upper().replace("А", "A").replace("Б", "B")
if number in tasks:
    tasks[number]()
else:
    print("Нет такого задания")
