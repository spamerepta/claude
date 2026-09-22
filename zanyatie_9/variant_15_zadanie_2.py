n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
best = None
best_sum = None
for row in a:
    if all(x % 2 != 0 for x in row):
        s = sum(abs(x) for x in row)
        if best_sum is None or s > best_sum:
            best_sum = s
            best = row
if best is None:
    print("Таких строк нет")
else:
    print(*best)
