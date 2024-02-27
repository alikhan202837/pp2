import re
#we need one Uppercase then at least one lower case letters
p = re.compile("[A-Z][a-z]+")

m1 = re.findall(p, "Abcd")
m2 = re.findall(p, "aAbcB")
m3 = re.findall(p, "aa1i31rf012=-AbcdfajfSjdna")
m4 = re.findall(p, "abdac1203rfk")

print(m1)
print(m2)
print(m3)
print(m4)



