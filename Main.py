import itertools

boardArray = []
boardArrayCombinations = []

def calculateArrangements(cube1, cube2, cube3, cube4, cube5, cube6, cube7, cube8, cube9):
    boardArray = [cube1, cube2, cube3, cube4, cube5, cube6, cube7, cube8, cube9]
    for combination in itertools.permutations(boardArray, len(boardArray)):
        boardArrayCombinations.append(combination)
    print(len(boardArrayCombinations))
    print(boardArrayCombinations)

calculateArrangements("lightBlue", "lightBlue", "lightBlue", "green", "green", "orange", "teal", "teal", "golden")
