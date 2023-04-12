import re


def regexStrip(input, removeChar='\s'):
    rawPattern = r'''
    ^
    %s*
    (.*?)
    %s*
    $
    ''' % (removeChar, removeChar)
    stringPattern = re.compile(rawPattern, re.VERBOSE)
    result = stringPattern.sub(r'\1', input)
    return result


defaultString = '  this has spaces around   '
beforeString = '  this has space before'
afterString = 'this has space after    '

alternative = '%this has percent around%'

print(regexStrip(defaultString))
print(regexStrip(beforeString))
print(regexStrip(afterString))
print(regexStrip(alternative, '%'))
