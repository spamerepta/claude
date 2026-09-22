n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
k = int(input())
count = 0
biggest = None
for row in a:
    for x in row:
        if x % k == 0:
            count += 1
            if biggest is None or x > biggest:
                biggest = x
print(count)
if biggest is None:
    print("Таких элементов нет")
else:
    print(biggest)
