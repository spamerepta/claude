fin = open("ФИО_группа_vvod.txt", encoding="utf-8")
fout = open("ФИО_группа_vivod.txt", "w", encoding="utf-8")


def read_line():
    return fin.readline()


def write(*args, **kwargs):
    print(*args, **kwargs, file=fout)


n = int(read_line())
a = [list(map(int, read_line().split())) for i in range(n)]
max_i, max_j = 0, 0
min_i, min_j = 0, 0
for i in range(n):
    for j in range(len(a[i])):
        if a[i][j] > a[max_i][max_j]:
            max_i, max_j = i, j
        if a[i][j] < a[min_i][min_j]:
            min_i, min_j = i, j
a[max_i][max_j], a[min_i][min_j] = a[min_i][min_j], a[max_i][max_j]
for row in a:
    write(*row)
fin.close()
fout.close()
