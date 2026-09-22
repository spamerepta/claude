n = int(input())
a = [float(input()) for i in range(n)]
average = sum(a) / n
for i in range(n):
    if a[i] == 0:
        a[i] = average
print(a)
