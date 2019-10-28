

def d(n):
    result = 0
    for i in range(1, n):
        if n % i == 0:
            result += i
    return result
                
count = 0
M = 10000

for a in range(1, M):
    b = d(a)
    if a != b and d(b) == a and b < M:
        count += a

print(count)
