def prime(n):
    cnt = 0
    for i in range(n + 1):
        if i >= 2 and n % i == 0:
            cnt += 1
    if cnt == 1:
        return True
    return False


a = [3,4,5,11,9,81,12,20,23,41]
primes = list(filter(prime, a))
print(primes)