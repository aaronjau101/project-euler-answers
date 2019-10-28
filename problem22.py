import csv

Names = []

with open('problem22file.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        Names.append(row)

A = []

for name in Names[0]:
    if (A == []):
        A.append(name)
    else:
        for i in range(0, len(A)):
            if name < A[i]:
                A.insert(i, name)
                break
            if(i == len(A) - 1):
                A.append(name)

count = 0
          
for x in range(0, len(A)):
    s = 0
    for i in A[x]:
        s += ord(i) - 64
    count += ((x+1) * s)

print(count)
