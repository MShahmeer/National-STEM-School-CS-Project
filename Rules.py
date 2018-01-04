#Rule for position of cube in certain column
def columnPosition(combination, position, colour, quantity):
    if position == "left":
        leftColumnArray = [combination[0], combination[3], combination[6]]
        matchingCubes = 0
        for cube in leftColumnArray:
            if cube == colour:
                matchingCubes += 1
        if matchingCubes >= quantity:
            return True
        else:
            return False
    elif position == "right":
        rightColumnArray = [combination[2], combination[5], combination[8]]
        matchingCubes = 0
        for cube in rightColumnArray:
            if cube == colour:
                matchingCubes += 1
        if matchingCubes >= quantity:
            return True
        else:
            return False
    elif position == "centre":
        centreColumnArray = [combination[1], combination[4], combination[7]]
        matchingCubes = 0
        for cube in centreColumnArray:
            if cube == colour:
                matchingCubes += 1
        if matchingCubes >= quantity:
            return True
        else:
            return False

#Rule for position of cube in certain row
def rowPosition(combination, position, colour, quantity):
    if position == "top":
        topRowArray = [combination[0], combination[1], combination[2]]
        matchingCubes = 0
        for cube in topRowArray:
            if cube == colour:
                matchingCubes += 1
        if matchingCubes >= quantity:
            return True
        else:
            return False
    elif position == "bottom":
        bottomRowArray = [combination[6], combination[7], combination[8]]
        matchingCubes = 0
        for cube in bottomRowArray:
            if cube == colour:
                matchingCubes += 1
        if matchingCubes >= quantity:
            return True
        else:
            return False
    elif position == "centre":
        centreRowArray = [combination[3], combination[4], combination[5]]
        matchingCubes = 0
        for cube in centreRowArray:
            if cube == colour:
                matchingCubes += 1
        if matchingCubes >= quantity:
            return True
        else:
            return False

#Rule for position of cubes in same row
# def sameRow(combination, colour1, colour2, colour3 = None):
#     topRowSet = {combination[0], combination[1], combination[2]}
#     bottomRowSet = {combination[6], combination[7], combination[8]}
#     centreRowSet = {combination[3], combination[4], combination[5]}
#     rows = [topRowSet, bottomRowSet, centreRowSet]
#     colours = [colour1, colour2, colour3]
#     for row in rows:
#         for colour in colours:
#             for cube in row:
#                 if colour3 == None:
#                     if colour2
#                 else:

#Rule for subject cube being between two others
def between(combination, colour1, colour2, colour3):
    possibleSubjectCubeIndexes = [1, 4, 7]
    for index in possibleSubjectCubeIndexes:
        if combination[index] != colour1:
            continue
        if combination[index-1] == colour2 and combination[index+1] == colour3) or \
            (combination[index-1] == colour3 and combination[index+1] == colour2):
            return True
    possibleSubjectCubeIndexes = [3, 4, 5]
    for index in possibleSubjectCubeIndexes:
        if combination[index] != colour1:
            continue
        if (combination[index-3] == colour2 and combination[index+3] == colour3) or \
            (combination[index-3] == colour3 and combination[index+3] == colour2):
            return True
    return False

#Rule for cubes touching each other
def touch(combination, ):
