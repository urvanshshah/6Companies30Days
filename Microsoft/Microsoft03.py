##3 : Rotate by 90 degree

def rotate(matrix):
    #code here
    n = len(matrix)
    for i in range(n//2):
        for j in range(i, n-i-1):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][n-1-i]
            matrix[j][n-1-i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[n-1-j][i]
            matrix[n-1-j][i] = tmp
