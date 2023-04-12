goodBoard = {
    '1h': 'bking',
    '6c': 'wqueen',
    '2g': 'bbishop',
    '5h': 'bqueen',
    '3e': 'wking'}
badBoardPrefix = {'1h': 'bking', '6c': 'wqueen',
                  '2g': 'bbishop', '5h': 'queen', '3e': 'wking'}
badBoardPiece = {'1h': 'bking', '6c': 'wqueen',
                 '2g': 'bbishop', '5h': 'wace', '3e': 'wking'}
badBoardPawnCount = {'1h': 'bking',
                     '6c': 'wqueen',
                     '2g': 'bbishop',
                     '5h': 'wace',
                     '3e': 'wking',
                     '2a': 'wpawn',
                     '2b': 'wpawn',
                     '2c': 'wpawn',
                     '2d': 'wpawn',
                     '2e': 'wpawn',
                     '2f': 'wpawn',
                     '3g': 'wpawn',
                     '2h': 'wpawn',
                     '3h': 'wpawn'}

badBoardGridNumber = {'1h': 'bking',
                      '6c': 'wqueen',
                      '2g': 'bbishop',
                      '9h': 'wpawn',
                      '3e': 'wking'}

badBoardGridLetter = {'1h': 'bking',
                      '6c': 'wqueen',
                      '2g': 'bbishop',
                      '3j': 'wpawn',
                      '3e': 'wking'}
badBoardKings = {
    '1h': 'bking',
    '2h': 'bking',
    '6c': 'wqueen',
    '2g': 'bbishop',
    '5h': 'bqueen',
    '3e': 'wking'}

goodBoardStartingPositions = {
    '1a': 'wrook',
    '1b': 'wknight',
    '1c': 'wbishop',
    '1d': 'wqueen',
    '1e': 'wking',
    '1f': 'wbishop',
    '1g': 'wknight',
    '1h': 'wrook',
    '2a': 'wpawn',
    '2b': 'wpawn',
    '2c': 'wpawn',
    '2d': 'wpawn',
    '2e': 'wpawn',
    '2f': 'wpawn',
    '2g': 'wpawn',
    '2h': 'wpawn',
    '8a': 'brook',
    '8b': 'bknight',
    '8c': 'bbishop',
    '8d': 'bqueen',
    '8e': 'bking',
    '8f': 'bbishop',
    '8g': 'bknight',
    '8h': 'brook',
    '7a': 'bpawn',
    '7b': 'bpawn',
    '7c': 'bpawn',
    '7d': 'bpawn',
    '7e': 'bpawn',
    '7f': 'bpawn',
    '7g': 'bpawn',
    '7h': 'bpawn',
}

badBoardStartingPositionsExtra = {
    '1a': 'wrook',
    '3a': 'wrook',
    '1b': 'wknight',
    '1c': 'wbishop',
    '1d': 'wqueen',
    '1e': 'wking',
    '1f': 'wbishop',
    '1g': 'wknight',
    '1h': 'wrook',
    '2a': 'wpawn',
    '2b': 'wpawn',
    '2c': 'wpawn',
    '2d': 'wpawn',
    '2e': 'wpawn',
    '2f': 'wpawn',
    '2g': 'wpawn',
    '2h': 'wpawn',
    '8a': 'brook',
    '8b': 'bknight',
    '8c': 'bbishop',
    '8d': 'bqueen',
    '8e': 'bking',
    '8f': 'bbishop',
    '8g': 'bknight',
    '8h': 'brook',
    '7a': 'bpawn',
    '7b': 'bpawn',
    '7c': 'bpawn',
    '7d': 'bpawn',
    '7e': 'bpawn',
    '7f': 'bpawn',
    '7g': 'bpawn',
    '7h': 'bpawn',
}


def isValidChessBoard(board):
    isValid = True

    validNumbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    validLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    pieceCount = {}
    for coord, value in board.items():
        color = value[0]
        piece = value[1:]
        pieceCount.setdefault(color, {})
        pieceCount[color].setdefault(piece, 0)
        pieceCount[color][piece] = pieceCount[color][piece] + 1
        coordNumber = coord[0]
        coordLetter = coord[1]

    # all pieces must be on a valid space from 1a to 8h
        if coordNumber not in validNumbers:
            isValid = False
        if coordLetter not in validLetters:
            isValid = False

    validColorPrefix = ['b', 'w']
    validPieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

    totals = {}
    for key, pieces in pieceCount.items():
        # limit of 1 bking and 1 wking
        if pieces.get('king', 0) > 1:
            isValid = False
        # at most 8 pawns
        if pieces.get('pawn', 0) > 8:
            isValid = False

        # each piece name begins with a w or b, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'
        if key not in validColorPrefix:
            isValid = False
        for piece, count in pieces.items():
            if piece not in validPieces:
                isValid = False
            totals.setdefault(key, 0)
            totals[key] = totals[key] + count

        for total in totals.values():
            # at most 16 pieces per player
            if total > 16:
                isValid = False

    # must return boolean
    return isValid


print(isValidChessBoard(goodBoard))
print(isValidChessBoard(badBoardPrefix))
print(isValidChessBoard(badBoardPiece))
print(isValidChessBoard(badBoardGridNumber))
print(isValidChessBoard(badBoardGridLetter))
print(isValidChessBoard(badBoardKings))
print(isValidChessBoard(badBoardPawnCount))
print(isValidChessBoard(goodBoardStartingPositions))
print(isValidChessBoard(badBoardStartingPositionsExtra))
