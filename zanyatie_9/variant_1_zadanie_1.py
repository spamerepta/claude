n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
total = 0
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i][j] > 0:
            total += a[i][j]
            count += 1
print(total, count)
