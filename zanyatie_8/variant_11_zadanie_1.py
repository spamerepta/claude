def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


n = int(input())
for i in range(n, 2 * n - 1):
    if is_prime(i) and is_prime(i + 2):
        print(i, i + 2)
