import math


def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


names = ["X", "Y", "Z", "P"]
points = []
for name in names:
    x = float(input())
    y = float(input())
    points.append((x, y))
best = -1
pair = ""
for i in range(4):
    for j in range(i + 1, 4):
        d = distance(points[i], points[j])
        if d > best:
            best = d
            pair = names[i] + " и " + names[j]
print(pair, best)
