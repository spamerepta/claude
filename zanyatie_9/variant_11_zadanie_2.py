n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
m = len(a[0])
best_j = None
best_product = None
for j in range(m):
    column = [a[i][j] for i in range(n)]
    if all(abs(x) <= 10 for x in column):
        product = 1
        for x in column:
            product *= x
        if best_product is None or product < best_product:
            best_product = product
            best_j = j
if best_j is None:
    print("Подходящих столбцов нет")
else:
    other = best_j + 1 if best_j + 1 < m else best_j - 1
    for row in a:
        row[best_j], row[other] = row[other], row[best_j]
    for row in a:
        print(*row)
