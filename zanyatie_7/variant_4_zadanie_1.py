n = int(input())
a = [int(input()) for i in range(n)]
biggest = max(a)
print(biggest, a.index(biggest) + 1)
