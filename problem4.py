num1 = 99;
num2 = 99;
      
def isPalindrome(n):
    s = str(n)
    f = 0
    l = len(s) - 1

    while(f < l):
        if(s[f] != s[l]):
            return False
        f += 1
        l -= 1
        
    return True

max = 0

for num1 in range(100, 1000):
    for num2 in range(100, 1000):
        if(isPalindrome(num1 * num2)):
            if max < num1 * num2:
                max = num1 * num2
print(max)
