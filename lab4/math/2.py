import math

def area_of_trapezoid(h, l, r):
    x = ((l + r)*h)/2
    return x

height = float(input("Height: "))
left = float(input("Base, first value: "))
right = float(input("Base, second value: "))

print(f"Expected Output: {area_of_trapezoid(height, left, right)}")

