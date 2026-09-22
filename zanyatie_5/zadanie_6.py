count = 0
total = 0
number = int(input())
while number != 0:
    count += 1
    total += number
    number = int(input())
print(total / count)
