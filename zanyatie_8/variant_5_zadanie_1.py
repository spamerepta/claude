def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


a = int(input())
b = int(input())
c = int(input())
d = int(input())
numerator = a * d - c * b
denominator = b * d
g = gcd(abs(numerator), denominator)
print(str(numerator // g) + "/" + str(denominator // g))
