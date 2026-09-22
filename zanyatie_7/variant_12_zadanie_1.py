n = int(input())
a = [int(input()) for i in range(n)]
odd = [x for x in a if x % 2 != 0]
if odd:
    print(min(odd))
else:
    print("Нечетных элементов нет")
