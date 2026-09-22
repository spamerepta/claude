n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
symmetric = True
for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i]:
            symmetric = False
if symmetric:
    print("Матрица симметрична")
else:
    print("Матрица не симметрична")
