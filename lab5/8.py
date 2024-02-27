import re

m = "bcdAsbnDskaOOOPoPoP"

new = ""

for i in range(len(m)):
    if m[i].isupper() != True:
        new += m[i]
    else:
        p = re.sub("[A-Z]", f" {m[i]}", m[i])
        new += p

new = new.split(" ")
print(new)






# --- 2nd method --- 
# def fun(s):
#     newstring = ""
#     for i in range(len(s)):
#         if s[i].isupper():
#             newstring += " " + s[i]
#         else:
#             newstring += s[i]
#     return newstring
            



# somestring = "AbcdEfghKOmlK"
# str2 = "bcdAsbnDskaOOOPoPoP"
# print(fun(somestring).strip())