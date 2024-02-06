primes = []
def filter_prime(a):
    for i in range(len(a)):
        cnt = 0
        for j in range(a[i] + 1):
            if j >= 2 and a[i] % j == 0:
                cnt+=1
        
        if cnt == 1:
            primes.append(a[i])
        


a = []
n = int(input("Size: "))
for i in range(n):
    x = int(input())
    a.append(x)



filter_prime(a)

primes.sort()

for i in primes:
    print(i, end = " ")