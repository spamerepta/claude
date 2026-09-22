n = int(input())
a = [int(input()) for i in range(n)]
repeated = []
for x in a:
    if a.count(x) > 1 and x not in repeated:
        repeated.append(x)
if repeated:
    print(*repeated)
else:
    print("Повторяющихся элементов нет")
