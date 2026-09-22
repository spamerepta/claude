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
    for j in range(len(a[i])):
        if a[i][j] > a[best_i][best_j]:
            best_i, best_j = i, j
a[0], a[best_i] = a[best_i], a[0]
for row in a:
    row[0], row[best_j] = row[best_j], row[0]
for row in a:
    write(*row)
fin.close()
fout.close()
