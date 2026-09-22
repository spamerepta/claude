fin = open("ФИО_группа_vvod.txt", encoding="utf-8")
fout = open("ФИО_группа_vivod.txt", "w", encoding="utf-8")


def read_line():
    return fin.readline()


def write(*args, **kwargs):
    print(*args, **kwargs, file=fout)


n = int(read_line())
a = [list(map(int, read_line().split())) for i in range(n)]
best = None
best_sum = None
for row in a:
    if all(x % 2 != 0 for x in row):
        s = sum(abs(x) for x in row)
        if best_sum is None or s > best_sum:
            best_sum = s
            best = row
if best is None:
    write("Таких строк нет")
else:
    write(*best)
fin.close()
fout.close()
