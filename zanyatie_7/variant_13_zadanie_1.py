n = int(input())
a = [int(input()) for i in range(n)]
found = False
checked = []
for x in a:
    if a.count(x) > 1 and x not in checked:
        checked.append(x)
        found = True
        indexes = [i for i in range(n) if a[i] == x]
        print(x, indexes)
if not found:
    print("Одинаковых элементов нет")
