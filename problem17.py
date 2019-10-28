import math

numberWords = ["one", "two", "three", "four", "five",
               "six", "seven", "eight", "nine", "ten",
               "eleven", "twelve", "thirteen", "fourteen", "fifteen",
               "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
               "thirty", "forty", "fifty", "sixty", "seventy",
               "eighty", "ninety"]

def NumberToWord(number):
    global numberWords
    word = ""
    if number <= 20:
        return numberWords[number - 1]
    elif number < 100:
        ten = math.floor(number / 10)
        word = numberWords[17 + ten]
        if number % 10 != 0:
            word += NumberToWord(number % 10)
        return word
    elif number < 1000:
        hundred = math.floor(number / 100)
        word = numberWords[hundred - 1] + "hundred"
        if number % 100 != 0:
            word += "and"
            word += NumberToWord(number % 100)
        return word
    else:
        return "Number Too High"

count = 0

for i in range(1, 1000):
    count += len(NumberToWord(i))
count += len("onethousand")    
print(count)
