s = input()
for word in s.split():
    word = word.strip('.,!?;:"()«»-')
    if word.startswith("а") or word.endswith("я"):
        print(word)
