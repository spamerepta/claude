n = int(input())
a = [list(map(float, input().split())) for i in range(n)]
best_i, best_j = 0, 0
for i in range(n):
    for j in (i, n - 1 - i):
        if a[i][j] > a[best_i][best_j]:
            best_i, best_j = i, j
c = n // 2
a[c][c], a[best_i][best_j] = a[best_i][best_j], a[c][c]
for row in a:
    print(*row)
