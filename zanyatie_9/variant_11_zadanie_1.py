n = int(input())
a = [list(map(float, input().split())) for i in range(n)]
best_i = 0
for i in range(n):
    if min(a[i]) < min(a[best_i]):
        best_i = i
print(sum(a[best_i]))
