import math

def toradians(x):
    x = x*(math.pi/180)
    return x


x = int(input("Input degree: "))


print(round(toradians(x), 6))
