count = 0


def check_point(x, y, a, b, r):
    global count
    if (x - a) ** 2 + (y - b) ** 2 < r ** 2:
        count += 1


a = float(input())
b = float(input())
r = float(input())
for i in range(3):
    x = float(input())
    y = float(input())
    check_point(x, y, a, b, r)
print(count)
