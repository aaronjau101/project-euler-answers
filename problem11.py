import csv

grid = []

with open('problem11file.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    for row in csv_reader:
        grid.append(row)

m = 0

for r in range(0, len(grid)):
    for c in range(0, len(grid[r])):
        if c + 3 < len(grid[r]) and r + 3 < len(grid):
            p = int(grid[r][c]) * int(grid[r+1][c+1]) * int(grid[r+2][c+2]) * int(grid[r+3][c+3])
            if m < p:
                m = p
        if c - 3 >= 0 and r + 3 < len(grid):
            p = int(grid[r][c]) * int(grid[r+1][c-1]) * int(grid[r+2][c-2]) * int(grid[r+3][c-3])
            if m < p:
                m = p
        if c + 3 < len(grid[r]):
            p = int(grid[r][c]) * int(grid[r][c+1]) * int(grid[r][c+2]) * int(grid[r][c+3])
            if m < p:
                m = p
        if r + 3 < len(grid):
            p = int(grid[r][c]) * int(grid[r+1][c]) * int(grid[r+2][c]) * int(grid[r+3][c])
            if m < p:
                m = p
print (m)




