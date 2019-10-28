old = 1
new = 2
s = 0
while(new < 4000000):
    temp = new
    new = old + new
    old = temp
    if(old % 2 == 0):
        s += old

print(s);
