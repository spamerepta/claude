n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
for row in a:
    row[0], row[-1] = row[-1], row[0]
for row in a:
    print(*row)
