a = [int(input()) for i in range(10)]
b = []
for x in a:
    if x not in b:
        b.append(x)
print(b)
