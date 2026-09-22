s = input()
for word in s.split():
    word = word.strip('.,!?;:"()«»-')
    if word.endswith("я"):
        print(word)
