n = int(input())
a = [float(input()) for i in range(n)]
smallest = a[0]
for x in a:
    if abs(x) < abs(smallest):
        smallest = x
print(smallest)
print(a[::-1])
