a = [int(input()) for i in range(15)]
b = a.copy()
for i in range(15):
    if b[i] < 10:
        b[i] = 0
    elif b[i] > 20:
        b[i] = 1
print(*a)
print(*b)
