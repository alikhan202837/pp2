import math

def area_of_parallelogram(l, h):
    S = l*h
    return S


length = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

print(f"Expected Output: {area_of_parallelogram(length, height)}")
