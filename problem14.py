def even(number):
    return number / 2

def odd(number):
    return (3 * number) + 1

maxChain = 1
indexOfMaxChain = 1

for i in range(2, 1000000):
    chain = 1
    number = i
    while number != 1: 
        if number % 2 == 0:
            number = even(number)
        else:
            number = odd(number)
        chain += 1
        
        if number < i:
            if number == indexOfMaxChain:
                indexOfMaxChain = i
                maxChain += chain
            break

    if chain > maxChain:
        maxChain = chain
        indexOfMaxChain = i

print(maxChain, indexOfMaxChain)




