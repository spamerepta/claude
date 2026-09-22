fin = open("ФИО_группа_vvod.txt", encoding="utf-8")
fout = open("ФИО_группа_vivod.txt", "w", encoding="utf-8")


def read_line():
    return fin.readline()


def write(*args, **kwargs):
    print(*args, **kwargs, file=fout)


n = int(read_line())
a = [list(map(int, read_line().split())) for i in range(n)]
for i in range(n):
    write("Строка", i + 1, "наибольший:", max(a[i]))
for j in range(n):
    column = [a[i][j] for i in range(n)]
    write("Столбец", j + 1, "наименьший:", min(column))
fin.close()
fout.close()
