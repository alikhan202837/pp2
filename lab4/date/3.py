import datetime

day = datetime.datetime.now()

print(f"With ms: {day}")
print("Without ms:", day.strftime("%Y-%m-%d %X"))

