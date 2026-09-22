fin = open("ФИО_группа_vvod.txt", encoding="utf-8")
fout = open("ФИО_группа_vivod.txt", "w", encoding="utf-8")


def read_line():
    return fin.readline()


def write(*args, **kwargs):
    print(*args, **kwargs, file=fout)


n = int(read_line())
b = list(map(int, read_line().split()))
a = [[0] * n for i in range(n)]
k = 0
for i in range(n):
    for j in range(i, n):
        a[i][j] = b[k]
        a[j][i] = b[k]
        k += 1
for row in a:
    write(*row)
fin.close()
fout.close()
