def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


n = int(input())
steps = 0
while n > 0:
    n -= digit_sum(n)
    steps += 1
print(steps)
