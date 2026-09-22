def same_color(x1, y1, x2, y2):
    if (x1 + y1) % 2 == (x2 + y2) % 2:
        print("Да")
    else:
        print("Нет")


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
same_color(x1, y1, x2, y2)
