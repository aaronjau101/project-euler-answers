number = pow(2, 1000)

string = str(number)

count = 0

for digit in string:
    count += int(digit)

print(count)
