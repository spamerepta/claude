n = int(input())
a = [int(input()) for i in range(n)]
even = [x for x in a if x % 2 == 0]
if even:
    print(max(even))
else:
    print("Четных элементов нет")
