import re


# for i in range(len(m)):
#     if m[i].isupper() == False:
#         print(m[i], end="")
#     else:
#         print(f" {m[i]}", end="")
# print()

m = "aBcdeFghiGklOMNpqrstUvWxYz"

new = ""

for i in range(len(m)):
    temp = ""
    if m[i].isupper() == False:
        new += m[i]
    else:
        temp += m[i]
        p = re.sub("[A-Z]", f" {temp}", temp)
        new += p
        
print(new)