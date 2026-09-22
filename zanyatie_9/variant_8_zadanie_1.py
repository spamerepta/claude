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
