fin = open("ФИО_группа_vvod.txt", encoding="utf-8")
fout = open("ФИО_группа_vivod.txt", "w", encoding="utf-8")


def read_line():
    return fin.readline()


def write(*args, **kwargs):
    print(*args, **kwargs, file=fout)


n = int(read_line())
a = [list(map(int, read_line().split())) for i in range(n)]
for row in a:
    i_max = row.index(max(row))
    row[0], row[i_max] = row[i_max], row[0]
    i_min = row.index(min(row))
    row[-1], row[i_min] = row[i_min], row[-1]
for row in a:
    write(*row)
fin.close()
fout.close()
