def print_min(a, b, c):
    smallest = a
    if b < smallest:
        smallest = b
    if c < smallest:
        smallest = c
    print(smallest)


a = int(input())
b = int(input())
c = int(input())
print_min(a, b, c)
