import re
#there we need one underscore and at least one lowercase letters before "_" and after "_"
p = "[a-z]+_[a-z]+"
"""
ab_cd -> ab_cd
ab_cd_ef_gh -> [ab_cd, ef_gh]
AB_CDef_gh_F -> ef_gh
"""
m = input("String: ")

m = re.findall(p, m)

print(m)
