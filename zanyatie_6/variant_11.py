s = input()
longest = 0
current = 0
for ch in s:
    if ch == "н":
        current += 1
        if current > longest:
            longest = current
    else:
        current = 0
print("Самая длинная последовательность букв н:", longest)
print(s.replace("!", "."))
