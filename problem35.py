from collections import deque

def getPrimes(N):
    A = [0] * (N + 1)

    primes = []
    A[0] = 1
    A[1] = 1
    P = 2
    while P < N + 1:
        primes.append(P)
        J = P * 2
        while J < N + 1:
            A[J] = 1
            J += P
        P += 1
        while P < N + 1 and A[P] != 0:
            P += 1
    return primes

def getRotations(T):
    R = []
    A = list(T)
    items = deque(A)
    for i in range(0, len(A)):
        items.rotate(1)
        R.append(list(items))
    return R


def isCircular(P):
    for combo in getRotations(str(P)):
        num = ""
        for c in combo:
           num += c
        num = int(num)
        if (num in primes) == False:
            return False  
    return True

result = 0
number = 1000000
primes = getPrimes(number)   

for prime in primes:
   if isCircular(prime):
       result += 1

print(result)




    





