fin = open("ФИО_группа_vvod.txt", encoding="utf-8")
fout = open("ФИО_группа_vivod.txt", "w", encoding="utf-8")


def read_line():
    return fin.readline()


def write(*args, **kwargs):
    print(*args, **kwargs, file=fout)


n = int(read_line())
a = [list(map(int, read_line().split())) for i in range(n)]
total = 0
count = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i][j] > 0:
            total += a[i][j]
            count += 1
write(total, count)
fin.close()
fout.close()
