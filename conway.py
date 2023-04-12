import random, time, copy

WIDTH = 60
HEIGHT = 20

nextCells = []

for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')
        else:
            column.append(' ')
    nextCells.append(column)
while True:
    print(time.asctime())
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')
        print()

    for x in range(WIDTH):
        for y in range(HEIGHT):

            # Get neighboring coordinates:
            # '% WIDTH' ensures leftCoord is always between 0 and width - 1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            numNeighbors = 0

            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # top left neighbor is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # top neighbor is alive
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # top right neighbor is alive
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # left neighbor is alive
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # right neighbor is alive
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # bottom left neighbor is alive
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # bottom neighbor is alive
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # bottom right neighbor is alive

            # set cell based on conway's game of life rules
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                # living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # dead cells with 3 neighbors become alive
                nextCells[x][y] = '#'
            else:
                #everything else either dies or stays dead
                nextCells[x][y] = ' '
    time.sleep(1)