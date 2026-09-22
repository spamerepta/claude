def print_digits(n):
    print(n % 10, end=" ")
    if n >= 10:
        print_digits(n // 10)


print_digits(int(input()))
print()
