n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
for row in a:
    row.sort()
for row in a:
    print(*row)
