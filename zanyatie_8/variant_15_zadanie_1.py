def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def is_binary_palindrome(n):
    binary = bin(n)[2:]
    return binary == binary[::-1]


n = int(input())
for i in range(2, n + 1):
    if is_prime(i) and is_binary_palindrome(i):
        print(i)
