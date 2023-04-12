import re
commaRegex = re.compile(r'''(
(^\d{1,3})# First group of numbers will be 1-3 digits long and at the start of the string
(,\d{3})* # Any subsequent groups will be lead by a comma
$ # the end of the string must come immediately after the full pattern. 
)''', re.VERBOSE)

print(commaRegex.search('42').group())
print(commaRegex.search('1,234').group())
print(commaRegex.search('6,368,745').group())

print(commaRegex.search('12,34,567') == None)
print(commaRegex.search('1234') == None)
