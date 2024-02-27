import re
#we have string where we have abb or abbb
pattern = re.compile("ab{2,3}")
"""
123abb123 -> abb
123abbbb321 -> abbb
123ab123 -> no

"""
m = input("String: ")

m = re.findall(pattern, m)

if len(m) == 0:
    print("It is no statisfy")
else: 
    print(m)

