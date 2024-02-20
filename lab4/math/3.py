import math

def area_of_polygon(n, len):
    S = int((n * len**2)/(4*math.tan(math.pi/n)))
    return S


n = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))

print(f"The area of the polygon is: {area_of_polygon(n, length)}")





