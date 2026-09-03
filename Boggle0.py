#Functions

def loadBoard(filename):
    with open (filename,'r') as file:
        Board = []

        for line in file:
            Board.append(line.strip().split())

    return Board

def printBoard(board):
    for row in board:
        print(" ".join(row))

    return row



myBoard = loadBoard("board.txt")
printBoard(myBoard)
#possibleMoves((0,0),myBoard)
#possibleMoves((2,2),myBoard)