import itertools
import Rules

boardArray = []
indexLabels = {0:"top-left", 1:"top-centre", 2:"top-right", 3:"centre-left", 4:"centre", 5:"centre-right", 6:"bottom-left", 7:"bottom-centre", 8:"bottom-right"}
gridArray = ["~", "~", "~", "~", "~", "~", "~", "~", "~"]
compatibleCombinations = []
solution = []

def printGrid(grid):
    print  (grid[0] + "|" + grid[1]  + "|" + grid[2])
    print ("-----")
    print (grid[3] + "|" + grid[4]  + "|" + grid[5])
    print ("-----")
    print (grid[6] + "|" + grid[7]  + "|" + grid[8])

def findGoldenCube(solution):
    index = -1
    for cube in solution:
        index += 1
        if cube == "golden":
            print("The golden cube is at the " + indexLabels[index] + " position.")

def solve(boardArray):
    for combination in itertools.permutations(boardArray, len(boardArray)):
        if Rules.columnPosition(combination, "left", "green", 2):
            if Rules.rowPosition(combination, "bottom", "teal", 2):
                if Rules.rowPosition(combination, "top", "lightBlue", 3):
                    if Rules.columnPosition(combination, "right", "orange", 1):
                        for cube in combination:
                            solution.append(cube)
                        findGoldenCube(solution)
                        break

solve(["lightBlue", "lightBlue", "lightBlue", "green", "green", "orange", "teal", "teal", "golden"])
