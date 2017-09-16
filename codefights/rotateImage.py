import copy

def rotateImage(a):
    n = len(a)
    b = copy.deepcopy(a)

    for i in range(0, int(n+1/2)):
        for j in range(0, n):
            print(i, j)
            b[i][j] = a[n-j-1][i]
            b[n-i-1][j]=a[n-j-1][n-i-1]

    print(a)
    print(b)


# a = [[1, 2, 3, 4],
#      [5, 6, 7, 8],
#      [9, 10, 11, 12],
#      [13, 14, 15, 16]]
#
# a = [[1, 2, 3, 4, 5],
#      [6, 7, 8, 9, 10],
#      [11, 12, 13, 14, 15],
#      [16, 17, 18, 19, 20],
#      [21, 22, 23, 24, 25]]

a = [[1,2,3],
    [4,5,6],
    [7,8,9]]

rotateImage(a)
