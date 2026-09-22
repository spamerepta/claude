def count_numbers(number, n, digits):
    count = 0
    if 100 <= number <= n:
        count += 1
    if number * 10 > n:
        return count
    for d in digits:
        if number * 10 + d > 0:
            count += count_numbers(number * 10 + d, n, digits)
    return count


n = int(input())
a = int(input())
b = int(input())
c = int(input())
digits = sorted(set([a, b, c]))
total = 0
for d in digits:
    if d != 0:
        total += count_numbers(d, n, digits)
print(total)
