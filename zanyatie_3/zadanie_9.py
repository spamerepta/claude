def can_break(n, m, k):
    if k < n * m and (k % n == 0 or k % m == 0):
        print("Да")
    else:
        print("Нет")


n = int(input())
m = int(input())
k = int(input())
can_break(n, m, k)
