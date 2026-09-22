fin = open("ФИО_группа_vvod.txt", encoding="utf-8")
fout = open("ФИО_группа_vivod.txt", "w", encoding="utf-8")


def read_line():
    return fin.readline()


def write(*args, **kwargs):
    print(*args, **kwargs, file=fout)


n = int(read_line())
a = [list(map(int, read_line().split())) for i in range(n)]
biggest = None
for row in a:
    if row == sorted(row) or row == sorted(row, reverse=True):
        if biggest is None or max(row) > biggest:
            biggest = max(row)
if biggest is None:
    write("Упорядоченных строк нет")
else:
    write(biggest)
fin.close()
fout.close()
