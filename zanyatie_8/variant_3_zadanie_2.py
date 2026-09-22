def sort_word(word):
    return "".join(sorted(word))


s = input()
print(" ".join(sort_word(word) for word in s.split()))
