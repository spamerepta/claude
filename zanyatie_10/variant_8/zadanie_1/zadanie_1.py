fin = open("ФИО_группа_vvod.txt", encoding="utf-8")
fout = open("ФИО_группа_vivod.txt", "w", encoding="utf-8")


def read_line():
    return fin.readline()


def write(*args, **kwargs):
    print(*args, **kwargs, file=fout)


n = int(read_line())
a = [list(map(float, read_line().split())) for i in range(n)]
k = int(read_line())
d = a[k - 1][k - 1]
if d == 0:
    write("Диагональный элемент равен нулю")
else:
    for j in range(n):
        a[k - 1][j] = a[k - 1][j] / d
for row in a:
    write(*row)
fin.close()
fout.close()
