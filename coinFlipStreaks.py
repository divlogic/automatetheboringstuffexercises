import random

numberOfStreaks = 0

def findStreak(flips):
    streaksCount = 0
    activeStreakLength = 0
    previousItem = None
    for index, currentItem in enumerate(flips):
        if currentItem == previousItem:
            activeStreakLength += 1
        else:
            activeStreakLength = 0

        if activeStreakLength == 5:
            streaksCount += 1
        previousItem = currentItem

    return streaksCount

for experimentNumber in range(10000):
    flips = []
    for flipNumber in range(100):
        currentFlip = random.randint(0, 1)
        flips.append(currentFlip)


    activeExperimentStreaks = findStreak(flips)
    if activeExperimentStreaks > 0:
        numberOfStreaks += 1



print('numberOfStreaks is: ' + str(numberOfStreaks))
print('Chance of streak: %s%%' % (numberOfStreaks / 10000))