n = int(input())
d = [int(input()) for i in range(n)]
total = 0
for i in range(1, n, 2):
    total += d[i]
print(d)
print(total)
