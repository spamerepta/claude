import math


def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 + (p[2] - q[2]) ** 2)


names = ["X", "Y", "Z", "T"]
points = []
for name in names:
    x = float(input())
    y = float(input())
    z = float(input())
    points.append((x, y, z))
best = None
pair = ""
for i in range(4):
    for j in range(i + 1, 4):
        d = distance(points[i], points[j])
        if best is None or d < best:
            best = d
            pair = names[i] + " и " + names[j]
print(pair, best)
