def print_range(a, b):
    print(a)
    if a < b:
        print_range(a + 1, b)
    elif a > b:
        print_range(a - 1, b)


a = int(input())
b = int(input())
print_range(a, b)
