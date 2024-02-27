import re
#we have string where we have "a" followed by something and end by "b"
p = re.compile(".*a.+b$")

m1 = re.match(p, "acb")
m2 = re.match(p, "vacgfhb")
m3 = re.match(p, "12a123bm") #error
print(m1.group())
print(m2.group())
print(m3.group())

