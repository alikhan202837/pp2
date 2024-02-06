import math
pi_val = math.pi
def volume(R):
    global pi_val
    V = (4/3)*pi_val*R**3
    return V

R = float(input("Radius: "))
print("Volume equal to {}".format(volume(R)))