a = [int(input()) for i in range(10)]
b = [int(input()) for i in range(10)]
for i in range(10):
    a[i], b[i] = b[i], a[i]
print(*a)
print(*b)
