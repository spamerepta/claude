fin = open("ФИО_группа_vvod.txt", encoding="utf-8")
fout = open("ФИО_группа_vivod.txt", "w", encoding="utf-8")


def read_line():
    return fin.readline()


def write(*args, **kwargs):
    print(*args, **kwargs, file=fout)


n = int(read_line())
a = [list(map(int, read_line().split())) for i in range(n)]
found = False
for k in range(n):
    if a[k] == [a[i][k] for i in range(n)]:
        write(k + 1)
        found = True
if not found:
    write("Таких k нет")
fin.close()
fout.close()
