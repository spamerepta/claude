age = int(input())
if age <= 0 or age >= 75:
    print("Некорректный возраст")
elif age >= 16:
    print("Поздравляем вы поступили в ВГУИТ")
else:
    print("Сначала нужно окончить школу!")
