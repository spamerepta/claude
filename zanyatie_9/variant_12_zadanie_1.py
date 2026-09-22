n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
found = False
for k in range(n):
    if a[k] == [a[i][k] for i in range(n)]:
        print(k + 1)
        found = True
if not found:
    print("Таких k нет")
