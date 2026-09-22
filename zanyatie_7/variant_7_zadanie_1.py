n = int(input())
a = [int(input()) for i in range(n)]
total = 0
product = 1
for i in range(n):
    if (i + 1) % 2 == 0:
        total += a[i]
    else:
        product *= a[i]
print(total, product)
