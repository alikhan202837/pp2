def histogram(number):
    for i in range(number):
        print("*", end = "")
    print()
    



n = int(input("Size of array: "))
a = []
for i in range(n):
    x = int(input())
    a.append(x)

for i in range(len(a)):
    histogram(a[i])

