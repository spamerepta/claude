import math


def angle(x, y):
    result = math.atan2(y, x)
    if result < 0:
        result += 2 * math.pi
    return result


def print_min_angle_point(points):
    best = points[0]
    for p in points:
        if angle(p[0], p[1]) < angle(best[0], best[1]):
            best = p
    print(best[0], best[1])


points = []
for i in range(3):
    x = float(input())
    y = float(input())
    points.append((x, y))
print_min_angle_point(points)
