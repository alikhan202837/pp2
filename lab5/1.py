import re


#we have string that have a or ab or abb and etc
p = re.compile(".*[ab*].*")
# "a" -> a
# "abbb" -> abbb
# "abbab" -> abb
# "as,nd,abb" -> a
# "nvjfvabb" -> nvjfvabb
# "nvanv" -> nvanv


m = input("String: ")
m = re.match(p, m)

if m == None:
    print("It not statisfy")
else:
    print(m.group())