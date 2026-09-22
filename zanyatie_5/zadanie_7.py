previous = int(input())
count = 0
if previous != 0:
    number = int(input())
    while number != 0:
        if number > previous:
            count += 1
        previous = number
        number = int(input())
print(count)
