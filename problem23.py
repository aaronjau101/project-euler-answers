def d(n):
    result = 0
    for i in range(1, n):
        if n % i == 0:
            result += i
    return result

def getAbundantNumbers(maxNumber):
    A = []
    if maxNumber <= 12:
        return A
    for i in range(12, maxNumber):
        if d(i) > i:
            A.append(i)
    return A

def getAbundantNumbersSum(maxNumber):
    D = [0] * maxNumber
    A = getAbundantNumbers(maxNumber)
    for b in A:
        for c in A:
            E = b + c
            if E < maxNumber:
                D[E] = 1
    return D

def f(n):
    A = getAbundantNumbersSum(n)
    S = 0
    for i in range(0, len(A)):
        if A[i] == 0:
            S += i
    return S

print(f(28124))




