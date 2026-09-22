n = int(input())
k = int(input())
a, b = 1, 1
total = 0
for i in range(1, k + n):
    if i >= k:
        total += a
    a, b = b, a + b
print(total)
