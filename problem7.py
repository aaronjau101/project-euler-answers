num = 2
i = 0



def isPrime(n):
    for a in range(2, round(n/2)):
       if(n % a == 0) :
           return False
    return True

while i < 10001:
    num += 1
    if(isPrime(num)):
        i += 1

print(num)
