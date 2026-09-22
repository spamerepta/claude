fin = open("ФИО_группа_vvod.txt", encoding="utf-8")
fout = open("ФИО_группа_vivod.txt", "w", encoding="utf-8")


def read_line():
    return fin.readline()


def write(*args, **kwargs):
    print(*args, **kwargs, file=fout)


n = int(read_line())
a = [list(map(float, read_line().split())) for i in range(n)]
best_i = 0
for i in range(n):
    if min(a[i]) < min(a[best_i]):
        best_i = i
write(sum(a[best_i]))
fin.close()
fout.close()
