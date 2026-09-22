s = input()
half = len(s) // 2
s = s[:half].replace("п", "*") + s[half:]
print(s)
