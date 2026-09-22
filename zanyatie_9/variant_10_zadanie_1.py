n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
biggest = None
for row in a:
    if row == sorted(row) or row == sorted(row, reverse=True):
        if biggest is None or max(row) > biggest:
            biggest = max(row)
if biggest is None:
    print("Упорядоченных строк нет")
else:
    print(biggest)
