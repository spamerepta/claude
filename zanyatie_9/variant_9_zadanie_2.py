n = int(input())
a = [list(map(float, input().split())) for i in range(n)]
best_i, best_j = 0, 0
for i in range(n):
    for j in range(n):
        if abs(a[i][j]) > abs(a[best_i][best_j]):
            best_i, best_j = i, j
b = []
for i in range(n):
    if i != best_i:
        b.append([a[i][j] for j in range(n) if j != best_j])
for row in b:
    print(*row)
