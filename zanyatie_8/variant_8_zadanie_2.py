def swap_first_last(a):
    a[0], a[-1] = a[-1], a[0]


m = int(input())
a = [int(input()) for i in range(m)]
print(a)
swap_first_last(a)
print(a)
