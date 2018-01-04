import itertools
import Rules

boardArray = []
#cubes = [cube1, cube2, cube3, cube4, cube5, cube6, cube7, cube8, cube9]
gridArray = ["~", "~", "~", "~", "~", "~", "~", "~", "~"]
compatibleCombinations = []

def printGrid(grid):
    print  (grid[0] + "|" + grid[1]  + "|" + grid[2])
    print ("-----")
    print (grid[3] + "|" + grid[4]  + "|" + grid[5])
    print ("-----")
    print (grid[6] + "|" + grid[7]  + "|" + grid[8])

def solve(boardArray):
    for combination in itertools.permutations(boardArray, len(boardArray)):
        if Rules.rowPosition(combination, "top", "green", 2):
            compatibleCombinations.append(combination)
    for combination in compatibleCombinations:
        print(combination)
    print(len(compatibleCombinations))

solve(["lightBlue", "lightBlue", "lightBlue", "green", "green", "orange", "teal", "teal", "golden"])
