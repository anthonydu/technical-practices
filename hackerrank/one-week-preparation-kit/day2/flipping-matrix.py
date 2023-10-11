#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#


def flippingMatrix(matrix):
    sum = 0
    n = len(matrix)
    # step through each ⿴
    for i in range(int(n / 2)):
        # add the max of the corners
        sum += max(
            matrix[i][i],
            matrix[i][n - i - 1],
            matrix[n - i - 1][i],
            matrix[n - i - 1][n - i - 1],
        )
        # step through the edges
        for j in range(i + 1, int(n / 2)):
            # add max of the edges (left & right cols)
            sum += max(
                matrix[j][i],
                matrix[n - j - 1][i],
                matrix[j][n - i - 1],
                matrix[n - j - 1][n - i - 1],
            )
            # add max of the edges (top & bottom rows)
            sum += max(
                matrix[i][j],
                matrix[i][n - j - 1],
                matrix[n - i - 1][j],
                matrix[n - i - 1][n - j - 1],
            )
    return sum
