def divisors_count(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


m = int(input())
n = int(input())
best = 0
numbers = []
for i in range(m, n + 1):
    count = divisors_count(i)
    if count > best:
        best = count
        numbers = [i]
    elif count == best:
        numbers.append(i)
print(*numbers)
print("Количество делителей:", best)
