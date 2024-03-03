s = input("String: ")

cntA = cnta = 0
for i in range(len(s)):
    if s[i].isupper() and s[i].isalpha():
        cntA += 1
    elif s[i].islower() and s[i].isalpha():
        cnta += 1
print("Number of Upper case:", cntA)
print("Number of lower case:", cnta)

    