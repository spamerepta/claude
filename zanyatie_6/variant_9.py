text = input()
word = input()
count = 0
for w in text.split():
    if w.strip('.,!?;:"()«»-').lower() == word.lower():
        count += 1
print(count)
