fin = open("ФИО_группа_vvod.txt", encoding="utf-8")
fout = open("ФИО_группа_vivod.txt", "w", encoding="utf-8")


def read_line():
    return fin.readline()


def write(*args, **kwargs):
    print(*args, **kwargs, file=fout)


n = int(read_line())
a = [list(map(float, read_line().split())) for i in range(n)]
best_i, best_j = 0, 0
for i in range(n):
    for j in range(n):
        if abs(a[i][j]) > abs(a[best_i][best_j]):
            best_i, best_j = i, j
b = []
for i in range(n):
    if i != best_i:
        b.append([a[i][j] for j in range(n) if j != best_j])
for row in b:
    write(*row)
fin.close()
fout.close()
