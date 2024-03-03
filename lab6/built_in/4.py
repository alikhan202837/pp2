import math
import time

number = int(input("Enter Number: "))
ms = int(input("Enter ms: "))

s = ms / 1000
time.sleep(s)

print("Square root of {} after {} miliseconds is".format(number, ms), math.sqrt(number))