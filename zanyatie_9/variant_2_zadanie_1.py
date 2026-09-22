n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
target = sum(a[0])
magic = True
for i in range(n):
    if sum(a[i]) != target:
        magic = False
    column = 0
    for j in range(n):
        column += a[j][i]
    if column != target:
        magic = False
if magic:
    print("Магический квадрат")
else:
    print("Не магический квадрат")
