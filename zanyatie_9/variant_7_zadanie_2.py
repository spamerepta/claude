n = int(input())
a = [list(map(float, input().split())) for i in range(n)]
diagonal = [a[i][i] for i in range(n)]
trace = sum(diagonal)
print(diagonal)
print(trace)
if trace == 0:
    print("След равен нулю, делить нельзя")
else:
    for i in range(1, n, 2):
        for j in range(n):
            a[i][j] = a[i][j] / trace
for row in a:
    print(*row)
