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

#Rule for subject cube being between two others
def between(combination, colour1, colour2, colour3):
    possibleSubjectCubeIndexes = [1, 4, 7]
    for index in possibleSubjectCubeIndexes:
        if combination[index] != colour1:
            continue
        if (combination[index-1] == colour2 and combination[index+1] == colour3) or \
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

#Rule for a cube in a certain direction
def direction(combination, action, colour1, colour2):
    if action == 'left':
        for cube in combination:
            if cube == colour1:
                index = combination.index(cube)
                if index == 1 or index == 4 or index == 7:
                    if combination[index-1] == colour2:
                        return True
                    else:
                        return False
                elif index == 2 or index == 5 or index == 8:
                    if combination[index-1] == colour2 or combination[index-2] == colour1:
                        return True
                    else:
                        return False
                else:
                    return False
    elif action == 'right':
         for cube in combination:
            if cube == colour1:
                index = combination.index(cube)
                if index == 1 or index == 4 or index == 7:
                    if combination[index+1] == colour2:
                        return True
                    else:
                        return False
                elif index == 0 or index == 3 or index == 6:
                    if combination[index+1] == colour2 or combination[index+2] == colour2:
                        return True
                    else:
                        return False
                else:
                    return False
    elif action == 'above':
        for cube in combination:
            if cube == colour1:
                index = combination.index(cube)
                if index-3 >= 0:
                    if combination[index-3] == colour2:
                        return True
                    elif index-6 >= 0 and combination[index-6] == colour2:
                        return True
                    else:
                        return False
    elif action == 'below':
        for cube in combination:
            if cube == color1:
                index = combination.index(cube)
                if index+3 <= 8:
                    print(value)
                    if combination[value+3] == color2:
                        return True
                    else:
                        return False
        for cube in combination:
            if cube == colour1:
                index = combination.index(cube)
                if index+3 >= 8:
                    if combination[index+3] == colour2:
                        return True
                    elif index+6 >= 6 and combination[index+6] == colour2:
                        return True
                    else:
                        return False

#Rule for position of cubes in same row
def sameRow(combination, colour1, colour2, colour3 = None):
    topRowSet = [combination[0], combination[1], combination[2]]
    bottomRowSet = [combination[6], combination[7], combination[8]]
    centreRowSet = [combination[3], combination[4], combination[5]]
    rows = [topRowSet, bottomRowSet, centreRowSet]
    colours = [colour1, colour2, colour3]
    if not colour3 == None:
        for row in rows:
            if set(row) == set(colours):
                return True
            else:
                return False
    else:
        for row in rows:
            colours.pop()
            if set(colours).issubset(set(row)):
                return True
            else:
                return False

def sameColumn(combination, colour1, colour2, colour3 = None):
    leftColumnSet = [combination[0], combination[3], combination[6]]
    rightColumnSet = [combination[2], combination[5], combination[8]]
    centreColumnSet = [combination[1], combination[4], combination[7]]
    columns = [leftColumnSet, rightColumnSet, centreColumnSet]
    colours = [colour1, colour2, colour3]
    if not colour3 == None:
        for column in columns:
            if set(column) == set(colours):
                return True
            else:
                return False
    else:
        for column in columns:
            colours.pop()
            if set(colours).issubset(set(column)):\
                return True
            else:
                return False

#Rule for cubes touching each other
# def touch(combination, colour1, quantity1 = 1, colour2, quantity2 = 1, colour3 = None, quantity3 = None, not = False):
#     indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#      for index in indexes:
#          if index == 0:
