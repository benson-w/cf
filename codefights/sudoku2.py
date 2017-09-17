def sudoku2(grid):
    n = len(grid)
    flag = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            if (grid[i][j] != "."):
                num = grid[i][j]

                # horizontal
                for m in range(0, i):
                    if (grid[m][j] == num): ## can probably just do && m != i, etc
                        print("false")
                        return 0
                for m in range(i+1, n):
                    if (grid[m][j] == num):
                        print("false")
                        return 0

                #vertical
                for k in range(0, j):
                    if (grid[i][k] == num):
                        print("false")
                        return 0
                for k in range(j+1, n):
                    if (grid[i][k] == num):
                        print("false")
                        return 0

                #9 by 9
                (i/3) * 3
                for y in range(int(i/3) * 3,int(i/3) * 3 + 3 ):
                    for z in range(int(j/3) * 3,int(j/3) * 3 + 3 ):
                        if (grid[y][z] == num) and ((y != i) and (z != j)):
                            print("false")
                            return 0



    print("true")
    return 1



grid1 = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

grid2 = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]

sudoku2(grid1)
