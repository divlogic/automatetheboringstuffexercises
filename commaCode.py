spam = ['apples', 'bananas', 'tofu', 'cats']

def stringifier(listToStringify):
    newString = ''
    for index, element in enumerate(listToStringify):
        if index == len(listToStringify) - 1:
            newString += 'and '

        newString += element
        if index < len(listToStringify) - 1:
            newString += ', '
    return newString

print(stringifier(spam))