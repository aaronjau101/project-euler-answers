N = int(pow(100, 100))

L = []

S = 0

for A in range(2, 101):
    for B in range(2, 101):
        C = pow(A, B)
        if (C in L) == False:
            L.append(C)
            S += 1

print (S)

