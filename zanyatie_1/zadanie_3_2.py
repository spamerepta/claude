name = input()
age = int(input())
if name == "Иван":
    print("Иван не может поступить")
elif age <= 0 or age >= 75:
    print("Некорректный возраст")
elif age >= 16:
    print("Поздравляем вы поступили в ВГУИТ")
else:
    print("Сначала нужно окончить школу!")
