def is_armstrong(number):
    n = len(str(number))
    total = 0
    x = number
    while x > 0:
        total += (x % 10) ** n
        x //= 10
    return total == number


k = int(input())
for i in range(1, k + 1):
    if is_armstrong(i):
        print(i)
