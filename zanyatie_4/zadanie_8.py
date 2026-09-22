n = int(input())
for i in range(1, n + 1):
    step = ""
    for j in range(1, i + 1):
        step += str(j)
    print(step)
