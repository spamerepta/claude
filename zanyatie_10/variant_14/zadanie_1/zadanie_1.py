fin = open("ФИО_группа_vvod.txt", encoding="utf-8")
fout = open("ФИО_группа_vivod.txt", "w", encoding="utf-8")


def read_line():
    return fin.readline()


def write(*args, **kwargs):
    print(*args, **kwargs, file=fout)


n = int(read_line())
a = [list(map(int, read_line().split())) for i in range(n)]
m = int(read_line())
best = 0
for i in range(n):
    if a[i][i] > a[best][best]:
        best = i
a[best], a[m - 1] = a[m - 1], a[best]
for row in a:
    write(*row)
fin.close()
fout.close()
