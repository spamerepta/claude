n = int(input())
a = [int(input()) for i in range(n)]
b = [x for x in a if x % 2 == 0 and x < 10]
if b:
    b.sort()
    print(b)
else:
    print("Таких чисел нет")
