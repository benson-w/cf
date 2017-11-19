f = []
file_ = open("in.txt", "r")
i = 0
for line in file_:
    if (line != ""):
        f.append(list(line))

print f
h = len(f)
w = len(f[0])

