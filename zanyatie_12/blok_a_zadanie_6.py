import sys

sys.setrecursionlimit(100000)


def is_prime(n, d=2):
    if d * d > n:
        return True
    if n % d == 0:
        return False
    return is_prime(n, d + 1)


n = int(input())
if is_prime(n):
    print("YES")
else:
    print("NO")
