a = [int(input()) for i in range(8)]
for i in range(8):
    if a[i] < 15:
        a[i] *= 2
print(a)
