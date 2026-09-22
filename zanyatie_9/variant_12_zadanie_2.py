n = int(input())
a = [list(map(float, input().split())) for i in range(n)]
for i in range(n - 1):
    for j in range(len(a[i])):
        a[i][j] -= a[n - 1][j]
for row in a:
    print(*row)
