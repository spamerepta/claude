m = int(input())
d = [list(map(int, input().split())) for i in range(m)]
k = int(input())
order = sorted(range(len(d[0])), key=lambda j: d[k - 1][j])
for row in d:
    print(*[row[j] for j in order])
