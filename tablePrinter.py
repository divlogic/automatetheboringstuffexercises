tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(data):
    colWidths = [0] * len(data)
    rowSize = len(data[0])
    formatted = [''] * rowSize

    for columnIndex, wordList in enumerate(data):
        for wordIndex, word in enumerate(wordList):
            length = len(word)
            if colWidths[columnIndex] < length:
                colWidths[columnIndex] = length

    for columnIndex, wordList in enumerate(data):
        for wordIndex, word in enumerate(wordList):
            formatted[wordIndex] += ' ' + data[columnIndex][wordIndex].rjust(
                colWidths[columnIndex])

    print('\n'.join(formatted))


printTable(tableData)
