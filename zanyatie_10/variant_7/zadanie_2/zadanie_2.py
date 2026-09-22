fin = open("ФИО_группа_vvod.txt", encoding="utf-8")
fout = open("ФИО_группа_vivod.txt", "w", encoding="utf-8")


def read_line():
    return fin.readline()


def write(*args, **kwargs):
    print(*args, **kwargs, file=fout)


n = int(read_line())
a = [list(map(float, read_line().split())) for i in range(n)]
diagonal = [a[i][i] for i in range(n)]
trace = sum(diagonal)
write(diagonal)
write(trace)
if trace == 0:
    write("След равен нулю, делить нельзя")
else:
    for i in range(1, n, 2):
        for j in range(n):
            a[i][j] = a[i][j] / trace
for row in a:
    write(*row)
fin.close()
fout.close()
