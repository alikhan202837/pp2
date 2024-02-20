import datetime

current = datetime.datetime.now()

yesterday = current - datetime.timedelta(days = 1)
tomorrow = current + datetime.timedelta(days = 1)

print(yesterday)
print(current)
print(tomorrow)