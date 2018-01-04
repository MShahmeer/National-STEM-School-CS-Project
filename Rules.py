#Rule for position of cube in certain column
def columnPosition(combination, position, colour, quantity):
    if position == "left":
        if combination[0] == colour and combination[3] == colour or combination[6] == colour:
            print(combination)
            return True
        else:
            return False
