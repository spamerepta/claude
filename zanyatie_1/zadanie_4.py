seconds = int(input())
days = seconds // 86400
hours = seconds % 86400 // 3600
minutes = seconds % 3600 // 60
secs = seconds % 60
print(str(days) + ":" + str(hours) + ":" + str(minutes) + ":" + str(secs))
