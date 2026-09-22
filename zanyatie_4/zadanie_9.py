n = int(input())
a, b = 1, 1
total = 0
for i in range(n):
    total += a
    a, b = b, a + b
print(total)
