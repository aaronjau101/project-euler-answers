import csv, math

grid = []

with open('problem13file.txt') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        grid.append(row)

numberSize = 50
tally = [];
index = 0;
carry = 0;
total = 0;

while index < numberSize or carry != 0:
    if index < numberSize:
        for row in grid:
            num = int(row[0][numberSize - 1 - index])
            total += num
        index += 1
    total += carry    
    tally.append(total % 10)
    carry = math.floor(total/10)
    total = 0

s = ""
for d in range(0, len(tally)):
    s += str(tally[len(tally) - d - 1])
    
print (s[0:10])






