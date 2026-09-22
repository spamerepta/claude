fin = open("ФИО_группа_vvod.txt", encoding="utf-8")
fout = open("ФИО_группа_vivod.txt", "w", encoding="utf-8")


def read_line():
    return fin.readline()


def write(*args, **kwargs):
    print(*args, **kwargs, file=fout)


n = int(read_line())
a = [list(map(int, read_line().split())) for i in range(n)]
k = int(read_line())
count = 0
biggest = None
for row in a:
    for x in row:
        if x % k == 0:
            count += 1
            if biggest is None or x > biggest:
                biggest = x
write(count)
if biggest is None:
    write("Таких элементов нет")
else:
    write(biggest)
fin.close()
fout.close()
