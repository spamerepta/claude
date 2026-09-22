def divisible_by_digits(number):
    x = number
    while x > 0:
        digit = x % 10
        if digit == 0 or number % digit != 0:
            return False
        x //= 10
    return True


n = int(input())
result = []
for i in range(1, n + 1):
    if divisible_by_digits(i):
        result.append(i)
print(*result)
