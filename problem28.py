spirals = 1
s = 2
n = 1
total = 1

while spirals < 1001:
    spirals += 2
    for i in range(1, 5):
        total += n + (s * i)
    n += s * 4
    s += 2

print (total)
    
    
