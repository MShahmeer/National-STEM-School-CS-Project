import Rules

def parseGameFile(fileName):
    fin = open(fileName)
    colors = fin.readline().split()
    fin.readline()
    rulesList = []
    for line in fin:
        rulesList.append(line.split())
    fin.close()
    return (colors, rulesList)

def parseRuleLines(rulesList, combination):
    result = False
    for rule in rulesList:
        if rule[0] == "column":
            result = Rules.columnPosition(combination, rule[1], rule[2], int(rule[3]))
            #print("1: " + str(combination))
        elif rule[0] == "row":
            result = Rules.rowPosition(combination, rule[1], rule[2], int(rule[3]))
            #print("1: " + str(combination))
        elif rule[0] == "sameRow":
            result = Rules.sameRow(combination, rule[1], rule[2])
            #print("1: " + str(combination))
        elif rule[0] == "sameColumn":
            result = Rules.sameColumn(combination, rule[1], rule[2], rule[3])
            #print("1: " + str(combination))
        elif rule[0] == "direction":
            result = Rules.direction(combination, rule[1], rule[2], rule[3])
            #print("1: " + str(combination))
        elif rule[0] == "between":
            result = Rules.between(combination, rule[1], rule[2], rule[3])
            #print("1: " + str(combination))
        elif rule[0] == "corner":
            result = Rules.corner(combination, rule[1], int(rule[2]), rule[3], rule[4])
            #print("1: " + str(combination))
        elif rule[0] == "touch":
            result = rules.touch(combination, rule[1], rule[2], rule[3])
            #print("1: " + str(combination))
        if result == False:
            return False
    return True
