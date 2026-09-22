def lace_length(a, b, l, n):
    return 2 * l + (2 * n - 1) * a + 2 * (n - 1) * b


a = int(input())
b = int(input())
l = int(input())
n = int(input())
print(lace_length(a, b, l, n))
