def power_div_factorial(x, n):
    if n == 0:
        return 1
    return power_div_factorial(x, n - 1) * x / n


x = int(input())
n = int(input())
print(power_div_factorial(x, n))
