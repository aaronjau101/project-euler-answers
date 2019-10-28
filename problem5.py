num = 2520;

def isDivisible(n):
    for i in range(11, 21):
        if(n % i != 0):
            return False
    return True

while(isDivisible(num) == False):
    num += 1

print(num)
