def eratosthenes(n):
    a = [1] * (n+1)
    a[0] = 0
    a[1] = 0
    p = 2
    
    while(pow(p, 2) <= n):
        j = pow(p, 2)
        while(j <= n):
            a[j] = 0
            j += p
        p += 1
        while(a[p] != 1):
            p += 1
    return a

primes = eratosthenes(2000000)

s = 0

for i in range(0, len(primes)):
    if(primes[i] == 1):
        s += i

print(s)


