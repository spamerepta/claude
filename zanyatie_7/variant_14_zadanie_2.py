a = [int(input()) for i in range(10)]
average = sum(a) / len(a)
print(average)
for i in range(10):
    if a[i] > average:
        a[i] = 1
print(a)
