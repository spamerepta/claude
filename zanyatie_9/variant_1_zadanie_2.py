n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
for row in a:
    i_max = row.index(max(row))
    row[0], row[i_max] = row[i_max], row[0]
    i_min = row.index(min(row))
    row[-1], row[i_min] = row[i_min], row[-1]
for row in a:
    print(*row)
