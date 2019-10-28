num1 = 0
num2 = 0

for i in range(1, 101):
    num1 += pow(i, 2)
    num2 += i

print(pow(num2, 2) - num1)
