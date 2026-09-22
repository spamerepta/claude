n = int(input())
a = [list(map(float, input().split())) for i in range(n)]
for row in a:
    i_min = row.index(min(row))
    if row[i_min] % 2 == 0:
        row[i_min] = 0
    else:
        row[i_min] = 1
for row in a:
    print(*row)
