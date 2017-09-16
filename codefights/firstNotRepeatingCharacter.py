def firstNotRepeatingCharacter(s):
    d = {}
    for i in range(0, len(s)):
        if s[i] in d:
            d[s[i]][0] = d[s[i]][0] + 1
        else:
            d[s[i]] = [1, i]
    print(d)

    ## look at the ones repeated 1 time, find smallest index
    a = 100000
    letter = "_"
    for key in d:
        if ((d[key][0] == 1) and (d[key][1] < a)):
            a = d[key][1]
            letter = key

    print letter
    return letter

#
s = "abcaebf"
firstNotRepeatingCharacter(s)
