import decimal

decimal.getcontext().prec = 500

def d(N):
    maxPattern = 0
    index = 0
    for i in range(2, N):
        A = str(decimal.Decimal(1)/decimal.Decimal(i))
        I = A.index(".")
        L = len(A)
        for k in range(1, L-1):
            pattern = A[k]
            for j in range(k + 1, L):
                if A[j] == pattern[0]:
                    E = len(pattern)
                    if A[j:j+E] == pattern:
                        if maxPattern < len(pattern):
                            maxPattern = len(pattern)
                            index = i    
                        break
                else:    
                    pattern += A[j]
    return index

print(d(1000))
            
