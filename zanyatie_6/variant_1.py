s = input()
count = 0
for word in s.split():
    word = word.strip('.,!?;:"()«»-')
    if word.lower().startswith("е"):
        count += 1
print(count)
