import math  

for a in range(1, 333):
    for b in range(2, 499):
        c = math.sqrt(pow(a, 2) + pow(b, 2))
        if(a < b and b < c and a + b + c == 1000):
            print(a * b * c)
            
