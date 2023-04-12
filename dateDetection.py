import re
#
# DD/MM/YYYY
# D goes from 01 to 31
# Months range from 01 to 12
# Years range from 1000 to 2999

dateRegex = re.compile(r'''(
    ([0-2][0-9]|3[0-1]) # DD
    / # separator
    (0[0-9]|1[0-2]) # MM
    \/ # separator
    ([1-2]\d\d\d) # YYYY
)''', re.VERBOSE)


def getMonthLength(month, year):
    year = int(year)
    monthLengths = {
        '01': 31,
        '02': 28,
        '03': 31,
        '04': 30,
        '05': 31,
        '06': 30,
        '07': 31,
        '08': 31,
        '09': 30,
        '10': 31,
        '11': 30,
        '12': 31,
    }
    if month != '02':
        return monthLengths[month]
    else:
        leapDays = 29
        divisibleByFour = year % 4 == 0
        divisibleByHundred = year % 100 == 0
        divisibleByFourHundred = year % 400 == 0
        if divisibleByFour:
            if divisibleByHundred and not divisibleByFourHundred:
                return monthLengths[month]
            if divisibleByHundred and divisibleByFourHundred:
                return leapDays

            return leapDays
        else:
            return monthLengths[month]


print('1999 ' + str(getMonthLength('02', '1999')))  # no leap year, so 28
print('1000 ' + str(getMonthLength('02', '1000')))  # no leap year, so 28
print('1000 ' + str(getMonthLength('02', '1996')))  # leap year so 29
print('2000 ' + str(getMonthLength('02', '2000')))  # leap year, so 29


def dateIsValid(date):
    results = dateRegex.search(date)
    if results != None:
        fullDate, day, month, year = results.groups()
        monthLength = getMonthLength(month, year)
        if int(day) > monthLength:
            return False
        return True
    else:
        return False


# valid
print(dateRegex.search('01/08/1981').group())
print(dateIsValid('01/08/1981'))  # valid
print(dateRegex.search('31/02/2020').group())
print(dateIsValid('31/02/2020'))  # invalid
print(dateRegex.search('31/04/2021').group())
print(dateIsValid('31/04/2021'))  # invalid
print(dateRegex.search('31/06/2021').group())
print(dateIsValid('31/06/2021'))  # invalid


# invalid
print(dateRegex.search('32/01/1999') == None)
print(dateRegex.search('12011999') == None)
print(dateRegex.search('01/01/0001') == None)
print(dateRegex.search('16/13/2012') == None)


# Doesn't have to validate correct days for month
# store these strings into variables named month, day and year.
# Write additional code to see if it is a valid date.
# April, June, September, and November have 30 days,
# February has 28 days,
#  and the rest of the months have 31 days.
# February has 29 days in leap years.
# Leap years are every year evenly divisible by 4,
# except for years evenly divisible by 100,
# unless the year is also evenly divisible by 400.
# Note how this calculation makes it impossible to
# make a reasonably sized regular expression that
# can detect a valid date.
