# there are some kinks to work out but it's good enough
import pyinputplus as pyip


def optionsWithPrices(options):
    menu = ''
    for key, price in options.items():
        menu += f'{key} {str(price)} '
    return menu


print('What kind of sandwich would you like?')
breadTypes = {'wheat': 0.30, 'white': 0.25, 'sourdough': 0.50}
proteinTypes = {'chicken': 0.50, 'turkey': 0.75, 'ham': 0.45, 'tofu': 0.50}
cheeseTypes = {'cheddar': 0.15, 'swiss': 0.15, 'mozzarella': 0.15}
extraTypes = {'mayo': 0, 'lettuce': 0, 'tomato': 0, 'mustard': 0.15}

breadPrompt = 'What kind of bread would you like?' + \
    optionsWithPrices(breadTypes) + '\n'
bread = pyip.inputMenu(list(breadTypes.keys()),
                       prompt=breadPrompt)

proteinPrompt = 'What kind of protein would you like? ' + \
    optionsWithPrices(proteinTypes) + '\n'
protein = pyip.inputMenu(list(proteinTypes.keys()),
                         prompt=proteinPrompt)
wantsCheese = pyip.inputYesNo('Would you like cheese?\n')
if wantsCheese == 'yes':
    cheesePrompt = 'What kind of cheese would you like? ' + \
        optionsWithPrices(cheeseTypes) + '\n'
    cheese = pyip.inputMenu(list(cheeseTypes.keys()), prompt=cheesePrompt)
extraChoices = []
for extra in extraTypes.keys():
    extraPrompt = 'Would you like ' + extra + \
        ' ? ' + str(extraTypes[extra]) + '\n'
    extraChoice = pyip.inputYesNo(extraPrompt)
    if extraChoice == 'yes':
        extraChoices.append(extra)
extrasSum = 0
for extra in extraChoices:
    extrasSum += extraTypes[extra]

sandwichPrice = breadTypes[bread] + \
    proteinTypes[protein] + cheeseTypes[cheese] + extrasSum

quantity = pyip.inputInt('How many sandwiches would you like?', min=1)

total = quantity * sandwichPrice

print('The total will be $' + str(total))
