import csv, math

A = []

with open('problem18file.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=" ")
    for row in csv_reader:
        A.append(row)

N = len(A)
B = []

def checkRoute(I, R, C):
    global B
    if R == N:
        B.append(C)
        return
    C += int(A[R][I])
    checkRoute(I, R + 1, C)
    checkRoute(I + 1, R + 1, C)

M = 0
checkRoute(0, 0, 0)

for number in B:
    if number > M:
        M = number


print(M)

