#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#


def gridChallenge(grid):
    for i in range(len(grid)):
        grid[i] = sorted(grid[i])
    for y in range(len(grid[0])):
        prev = "a"
        for x in range(len(grid)):
            if grid[x][y] < prev:
                return "NO"
            else:
                prev = grid[x][y]
    return "YES"
