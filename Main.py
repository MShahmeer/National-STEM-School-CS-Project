import itertools
import Rules
import Parser

from termcolor import colored

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
            text = "The golden cube is at the " + indexLabels[index] + " position."
            print(colored(text, "red", "on_yellow"))

def solve(fileName):
    solution = []
    boardArray, rulesList = Parser.parseGameFile(fileName)
    print(rulesList)
    for combination in itertools.permutations(boardArray, len(boardArray)):
        #print(combination)
        if Parser.parseRuleLines(rulesList, combination):
            return combination

findGoldenCube(solve("1.txt"))
