N = 100
F = 1
S = 0
string = ""

for number in range(2, N):
    F *= number

string = str(F)

for number in string:
    S += int(number)

print(S)
