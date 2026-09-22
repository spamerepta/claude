def remainder(a, b):
    if a < b:
        return a
    return remainder(a - b, b)


a = int(input())
b = int(input())
print(remainder(a, b))
