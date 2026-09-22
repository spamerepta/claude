def to_octal(n):
    result = ""
    for i in range(10):
        result = str(n % 8) + result
        n //= 8
    return result


print(to_octal(int(input())))
