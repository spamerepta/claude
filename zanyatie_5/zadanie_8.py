previous = int(input())
current_length = 1
max_length = 1
number = int(input()) if previous != 0 else 0
while number != 0:
    if number == previous:
        current_length += 1
    else:
        current_length = 1
    if current_length > max_length:
        max_length = current_length
    previous = number
    number = int(input())
print(max_length)
