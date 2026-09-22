s = input()
s = s[:-1] if s.endswith(".") else s
print(len(s.split()))
