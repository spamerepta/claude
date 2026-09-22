n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
for i in range(1, n, 2):
    print("Строка", i + 1, ":", min(a[i]))
