import itertools
import Rules

boardArray = []
indexLabels = {0:"top-left", 1:"top-centre", 2:"top-right", 3:"centre-left", 4:"centre", 5:"centre-right", 6:"bottom-left", 7:"bottom-centre", 8:"bottom-right"}
gridArray = ["~", "~", "~", "~", "~", "~", "~", "~", "~"]
compatibleCombinations = []

def printGrid(grid):
    print  (grid[0] + "|" + grid[1]  + "|" + grid[2])
    print ("-----")
    print (grid[3] + "|" + grid[4]  + "|" + grid[5])
    print ("-----")
    print (grid[6] + "|" + grid[7]  + "|" + grid[8])

def findGoldenCube(solution):
    print(solution)
    index = -1
    for cube in solution:
        index += 1
        if cube == "golden":
            print("The golden cube is at the " + indexLabels[index] + " position.")

def solve(boardArray):
    solution = []
    i = 0
    for combination in itertools.permutations(boardArray, len(boardArray)):
        if Rules.between(combination, "green", "orange", "golden"):
            return combination

#findGoldenCube(solve(["lightBlue", "lightBlue", "lightBlue", "green", "green", "orange", "teal", "teal", "golden"]))
solve(["lightBlue", "lightBlue", "lightBlue", "green", "green", "orange", "teal", "teal", "golden"])
