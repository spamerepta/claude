n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
t = [[a[i][j] for i in range(n)] for j in range(n)]
for row in t:
    print(*row)
