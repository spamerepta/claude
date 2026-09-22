n = int(input())
a = [int(input()) for i in range(n)]
positive = []
other = []
for x in a:
    if x > 0:
        positive.append(x)
    else:
        other.append(x)
print(positive)
print(other)
