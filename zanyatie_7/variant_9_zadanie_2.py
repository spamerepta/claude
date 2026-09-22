a = [int(input()) for i in range(10)]
b = [int(input()) for i in range(10)]
print(a)
print(b)
a, b = b, a
print(*a)
print(*b)
