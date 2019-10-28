num = 600851475143
totalPrimes = [];

def getPrimes(n):
    i = 2
    while i < n:
        if(n % i == 0):
            return i
        i += 1
    return 0

while getPrimes(num) != 0:
    totalPrimes.append(getPrimes(num))
    num /= getPrimes(num)

totalPrimes.append(num)

print(totalPrimes)


