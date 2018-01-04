#Rule for position of cube in certain column
def columnPosition(combination, position, colour, quantity):
    if position == "left":
        leftColumnArray = [combination[0], combination[3], combination[6]]
        matchingCubes = 0
        for cube in leftColumnArray:
            if cube == colour:
                matchingCubes += 1
            else:
                pass
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
            else:
                pass
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
            else:
                pass
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
            else:
                pass
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
            else:
                pass
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
            else:
                pass
        if matchingCubes >= quantity:
            return True
        else:
            return False
