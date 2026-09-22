n = int(input())
a = [int(input()) for i in range(n)]
i_min = a.index(min(a))
i_max = a.index(max(a))
a[i_min], a[i_max] = a[i_max], a[i_min]
print(a)
