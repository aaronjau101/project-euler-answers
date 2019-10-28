def isLeapYear(year):
    badCentury = year % 100 == 0 and year % 400 != 0
    return year % 4 == 0 and not badCentury

def getDay(date):
    global count
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0
    D = 1
    M = 0
    Y = 1900
    while [D, M, Y] != date:
        day = (day + 1) % 7
        D += 1
        month = months[M]
        if M == 1 and isLeapYear(Y):
            month = 29
        if D > month:
            D = 1
            M += 1
            if M == len(months):
                M = 0
                Y += 1
        if day == 6 and D == 1 and Y > 1900:
            count += 1
    return day

count = 0
getDay([31, 11, 2000])
print(count)

