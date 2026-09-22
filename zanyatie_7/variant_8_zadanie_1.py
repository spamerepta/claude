n = int(input())
a = [int(input()) for i in range(n)]
product = 1
for x in a:
    product *= x
print("Сумма:", sum(a))
print("Произведение:", product)
