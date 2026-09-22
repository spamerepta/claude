n = int(input())
power = 0
value = 1
while value * 2 <= n:
    value *= 2
    power += 1
print(power, value)
