fin = open("ФИО_группа_vvod.txt", encoding="utf-8")
fout = open("ФИО_группа_vivod.txt", "w", encoding="utf-8")


def read_line():
    return fin.readline()


def write(*args, **kwargs):
    print(*args, **kwargs, file=fout)


n = int(read_line())
a = [list(map(int, read_line().split())) for i in range(n)]
sums = [sum(row) for row in a]
i_max = sums.index(max(sums))
i_min = sums.index(min(sums))
write("Наибольшая сумма:", *a[i_max], "сумма", sums[i_max])
write("Наименьшая сумма:", *a[i_min], "сумма", sums[i_min])
fin.close()
fout.close()
