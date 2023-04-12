import re


def isStrongPassword(password):
    # at least 8 characters long
    if len(password) < 8:
        return False
    # contains both uppercase and lowercase characters
    if re.compile(r'[a-z]').search(password) == None:
        return False
    if re.compile(r'[A-Z]').search(password) == None:
        return False
    # has at least one digit
    if re.compile(r'\d').search(password) == None:
        return False

    return True


weakShort = 'pass12'
weakLong = 'longpasswordlowercase'
weakNoNumber = 'passwordTEST'
weakNoCaps = 'password12345'
weakNoLower = 'PASSWORD12345'

strong = 'ThisIsP4ssw0rd'

print(weakShort, isStrongPassword(weakShort))
print(weakLong, isStrongPassword(weakLong))
print(weakNoNumber, isStrongPassword(weakNoNumber))
print(weakNoCaps, isStrongPassword(weakNoCaps))
print(weakNoLower, isStrongPassword(weakNoLower))
print(strong, isStrongPassword(strong))
