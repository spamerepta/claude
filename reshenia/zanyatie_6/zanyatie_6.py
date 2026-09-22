def variant_8():
    s = input()
    s = s[:-1] if s.endswith(".") else s
    print(len(s.split()))


tasks = {
    "8": variant_8,
}
number = input("Номер задания (8): ").strip()
if number in tasks:
    tasks[number]()
else:
    print("Нет такого задания")
