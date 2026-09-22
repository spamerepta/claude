fin = open("ФИО_группа_vvod.txt", encoding="utf-8")
fout = open("ФИО_группа_vivod.txt", "w", encoding="utf-8")


def read_line():
    return fin.readline()


def write(*args, **kwargs):
    print(*args, **kwargs, file=fout)


n = int(read_line())
a = [list(map(int, read_line().split())) for i in range(n)]
target = sum(a[0])
magic = True
for i in range(n):
    if sum(a[i]) != target:
        magic = False
    column = 0
    for j in range(n):
        column += a[j][i]
    if column != target:
        magic = False
if magic:
    write("Магический квадрат")
else:
    write("Не магический квадрат")
fin.close()
fout.close()
