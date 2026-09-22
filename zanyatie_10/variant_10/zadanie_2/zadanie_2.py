fin = open("ФИО_группа_vvod.txt", encoding="utf-8")
fout = open("ФИО_группа_vivod.txt", "w", encoding="utf-8")


def read_line():
    return fin.readline()


def write(*args, **kwargs):
    print(*args, **kwargs, file=fout)


m = int(read_line())
d = [list(map(int, read_line().split())) for i in range(m)]
k = int(read_line())
order = sorted(range(len(d[0])), key=lambda j: d[k - 1][j])
for row in d:
    write(*[row[j] for j in order])
fin.close()
fout.close()
