#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                sum1 += arr[i][j]
            if i + j == len(arr) - 1:
                sum2 += arr[i][j]
    return abs(sum1 - sum2)
