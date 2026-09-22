def reverse(n, result=0):
    if n == 0:
        return result
    return reverse(n // 10, result * 10 + n % 10)


print(reverse(int(input())))
