n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        if a[i][j] < 0:
            a[i][j] = 0
        elif a[i][j] > 0:
            a[i][j] = 1
for i in range(n):
    for j in range(n):
        if j <= i:
            print(a[i][j], end=" ")
        else:
            print(0, end=" ")
    print()
