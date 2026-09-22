fin = open("ФИО_группа_vvod.txt", encoding="utf-8")
fout = open("ФИО_группа_vivod.txt", "w", encoding="utf-8")


def read_line():
    return fin.readline()


def write(*args, **kwargs):
    print(*args, **kwargs, file=fout)


n = int(read_line())
a = [list(map(int, read_line().split())) for i in range(n)]
symmetric = True
for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i]:
            symmetric = False
if symmetric:
    write("Матрица симметрична")
else:
    write("Матрица не симметрична")
fin.close()
fout.close()
