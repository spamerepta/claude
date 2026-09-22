a = [int(input()) for i in range(10)]
for i in range(9):
    if a[i] < 0 and a[i + 1] < 0:
        print(a[i], a[i + 1])
