n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
sums = [sum(row) for row in a]
i_max = sums.index(max(sums))
i_min = sums.index(min(sums))
print("Наибольшая сумма:", *a[i_max], "сумма", sums[i_max])
print("Наименьшая сумма:", *a[i_min], "сумма", sums[i_min])
