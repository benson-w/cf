def isCryptSolution(crypt, solution):
    w1 = crypt[0]
    w2 = crypt[1]
    w3 = crypt[2]

    if (checkFirst(w1, solution) == 1) or (checkFirst(w2, solution) == 1):
        print("false")
        return 0

    if calculateVal(w1, solution) + calculateVal(w2, solution) == calculateVal(w3, solution):
        print("true")
        return 1
    else:
        print("false")
        return 0

def checkFirst(s, solution):
    for j in range(0, len(solution)):
        if (solution[j][0] == s[0]) and (int(solution[j][1]) == 0) and (len(s) != 1):
            return 1
    return 0

def calculateVal(s, solution):
    total = 0
    for i in range(0, len(s)):
        for j in range(0, len(solution)):
            if (solution[j][0] == s[i]):
                total = total + (int(solution[j][1]) * (10 ** (len(s) - i - 1)))
    return total

# solution = [['O', '0'],
#             ['M', '1'],
#             ['Y', '2'],
#             ['E', '5'],
#             ['N', '6'],
#             ['D', '7'],
#             ['R', '8'],
#             ['S', '9']]
#
# crypt = ["SEND", "MORE", "MONEY"]

# solution = [['O', '1'],
#             ['T', '0'],
#             ['W', '9'],
#             ['E', '5'],
#             ['N', '4']]
#
# crypt = ["TEN", "TWO", "ONE"]

solution = [["A","0"]]

crypt = ["A",
 "A",
 "A"]

isCryptSolution(crypt, solution)
