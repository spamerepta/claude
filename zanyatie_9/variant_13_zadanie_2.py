n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
max_i, max_j = 0, 0
min_i, min_j = 0, 0
for i in range(n):
    for j in range(len(a[i])):
        if a[i][j] > a[max_i][max_j]:
            max_i, max_j = i, j
        if a[i][j] < a[min_i][min_j]:
            min_i, min_j = i, j
a[max_i][max_j], a[min_i][min_j] = a[min_i][min_j], a[max_i][max_j]
for row in a:
    print(*row)
