n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    print("Строка", i + 1, "наибольший:", max(a[i]))
for j in range(n):
    column = [a[i][j] for i in range(n)]
    print("Столбец", j + 1, "наименьший:", min(column))
