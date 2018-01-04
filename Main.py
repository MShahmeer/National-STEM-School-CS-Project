import itertools
import Rules

boardArray = []
boardArrayCombinations = []
gridArray = ["~", "~", "~", "~", "~", "~", "~", "~", "~"]
solutionFound = False

def printGrid(grid):
    print  (grid[0] + "|" + grid[1]  + "|" + grid[2])
    print ("-----")
    print (grid[3] + "|" + grid[4]  + "|" + grid[5])
    print ("-----")
    print (grid[6] + "|" + grid[7]  + "|" + grid[8])

def calculateArrangements(cube1, cube2, cube3, cube4, cube5, cube6, cube7, cube8, cube9):
    boardArray = [cube1, cube2, cube3, cube4, cube5, cube6, cube7, cube8, cube9]
    for combination in itertools.permutations(boardArray, len(boardArray)):
        boardArrayCombinations.append(combination)
    #print(len(boardArrayCombinations))
    #print(boardArrayCombinations)

calculateArrangements("lightBlue", "lightBlue", "lightBlue", "green", "green", "orange", "teal", "teal", "golden")

for combination in boardArrayCombinations:
    solutionFound = Rules.columnPosition(combination, "left", "green", 2)
    print(solutionFound)
    if solutionFound == True:
        print(combination)
        break
    else:
        pass
