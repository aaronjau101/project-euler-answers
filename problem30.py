import sys
N = 400000
T = 0

for A in range(10, N):
    S = str(A)
    C = 0
    for I in S:
        C += pow(int(I), 5)
    if A == C:
        T += A
    
print(T)
