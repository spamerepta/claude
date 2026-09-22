n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
c = int(input())
d = int(input())
rows = []
for i in range(n):
    if c in a[i]:
        rows.append(i + 1)
        for j in range(len(a[i])):
            a[i][j] *= d
print(*rows)
for row in a:
    print(*row)
