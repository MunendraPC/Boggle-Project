#Functions

def loadBoard(filename):
    with open (filename,'r') as file:
        Board = []

        for line in file:
            print(line().strip().split())

    