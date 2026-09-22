import sys

sys.setrecursionlimit(100000)


def is_prime(n, d=3):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if d * d > n:
        return True
    if n % d == 0:
        return False
    return is_prime(n, d + 2)


n = int(input())
if is_prime(n):
    print("YES")
else:
    print("NO")
