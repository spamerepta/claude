fin = open("ФИО_группа_vvod.txt", encoding="utf-8")
fout = open("ФИО_группа_vivod.txt", "w", encoding="utf-8")


def read_line():
    return fin.readline()


def write(*args, **kwargs):
    print(*args, **kwargs, file=fout)


n = int(read_line())
a = [[0] * n for i in range(n)]
top, bottom, left, right = 0, n - 1, 0, n - 1
number = 1
while number <= n * n:
    for j in range(left, right + 1):
        a[top][j] = number
        number += 1
    top += 1
    for i in range(top, bottom + 1):
        a[i][right] = number
        number += 1
    right -= 1
    for j in range(right, left - 1, -1):
        a[bottom][j] = number
        number += 1
    bottom -= 1
    for i in range(bottom, top - 1, -1):
        a[i][left] = number
        number += 1
    left += 1
for row in a:
    write(*row)
fin.close()
fout.close()
