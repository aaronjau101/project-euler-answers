def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def quadratic(a, b, n):
    return (pow(n, 2) + (a * n) + b)

def getN(a, b):
    n = 0
    while isPrime(quadratic(a, b, n)):
        n += 1
    return n

def f():
    M = 0
    AM = 0
    BM = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = getN(a, b)
            if M < n:
                M = n
                AM = a
                BM = b
    print(AM * BM)

f()
