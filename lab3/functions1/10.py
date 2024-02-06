unique = []
def unique_list(a):
    a.sort()
    for i in range(len(a)):
        cnt = 0
        for j in range(len(a)):
            if j >= i + 1 and a[i] == a[j]:
                cnt += 1
            if i == len(a) - 1:
                break
        if cnt == 0:
            unique.append(a[i])


a = []
n = int(input("Size: "))
for i in range(n):
    x = int(input())
    a.append(x)
unique_list(a)


print(unique)