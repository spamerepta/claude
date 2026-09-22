fin = open("ФИО_группа_vvod.txt", encoding="utf-8")
fout = open("ФИО_группа_vivod.txt", "w", encoding="utf-8")


def read_line():
    return fin.readline()


def write(*args, **kwargs):
    print(*args, **kwargs, file=fout)


n = int(read_line())
a = [list(map(int, read_line().split())) for i in range(n)]
c = int(read_line())
d = int(read_line())
rows = []
for i in range(n):
    if c in a[i]:
        rows.append(i + 1)
        for j in range(len(a[i])):
            a[i][j] *= d
write(*rows)
for row in a:
    write(*row)
fin.close()
fout.close()
