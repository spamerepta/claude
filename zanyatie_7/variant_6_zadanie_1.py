a = [int(input()) for i in range(10)]
average = sum(a) / len(a)
less = 0
greater = 0
for x in a:
    if x < average:
        less += 1
    elif x > average:
        greater += 1
print("Среднее арифметическое:", average)
print("Меньше среднего:", less)
print("Больше среднего:", greater)
