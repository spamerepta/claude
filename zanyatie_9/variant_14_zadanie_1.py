n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
m = int(input())
best = 0
for i in range(n):
    if a[i][i] > a[best][best]:
        best = i
a[best], a[m - 1] = a[m - 1], a[best]
for row in a:
    print(*row)
