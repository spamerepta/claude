n = int(input())
b = list(map(int, input().split()))
a = [[0] * n for i in range(n)]
k = 0
for i in range(n):
    for j in range(i, n):
        a[i][j] = b[k]
        a[j][i] = b[k]
        k += 1
for row in a:
    print(*row)
