def divisors_sum(n):
    total = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1
    return total


n = int(input())
for a in range(2, n + 1):
    b = divisors_sum(a)
    if a < b <= n and divisors_sum(b) == a:
        print(a, b)
