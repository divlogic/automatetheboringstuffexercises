import re

sentenceRegex = re.compile(r'''(
(alice|bob|carol)
\s
(eats|pets|throws)
\s
(apples|cats|baseballs)
\.
)''', re.VERBOSE | re.IGNORECASE)

print(sentenceRegex.search('Alice eats apples.').group())
print(sentenceRegex.search('Bob pets cats.').group())
print(sentenceRegex.search('Carol throws baseballs.').group())
print(sentenceRegex.search('Alice throws Apples.').group())
print(sentenceRegex.search('BOB EATS CATS.').group())

print(sentenceRegex.search('RoboCop eats apples.') == None)
print(sentenceRegex.search('ALICE THROWS FOOTBALLS.') == None)
print(sentenceRegex.search('Carol eats 7 cats.') == None)
