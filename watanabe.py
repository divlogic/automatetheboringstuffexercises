import re
watanabeRegex = re.compile(r'''(
^[A-Z][a-zA-Z]+ # First name, starts capital, then either capital or lowercase 
\s # single space in between
Watanabe
$
)''', re.VERBOSE)


print(watanabeRegex.search('Haruto Watanabe').group())
print(watanabeRegex.search('Alice Watanabe').group())
print(watanabeRegex.search('RoboCop Watanabe').group())

# (where the first name is not capitalized)
# (where the preceding word has a nonletter character)
# (which has no first name)
# (where Watanabe is not capitalized)
print(watanabeRegex.search('haruto Watanabe') == None)
print(watanabeRegex.search('Mr. Watanabe') == None)
print(watanabeRegex.search('Watanabe') == None)
print(watanabeRegex.search('Haruto watanabe') == None)
