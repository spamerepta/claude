def two_largest():
    n = int(input())
    if n == 0:
        return 0, 0
    first, second = two_largest()
    if n > first:
        return n, first
    if n > second:
        return first, n
    return first, second


first, second = two_largest()
print(second)
