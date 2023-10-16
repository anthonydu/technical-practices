#
# Complete the 'subsetA' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def subsetA(arr):
    n = len(arr)
    arr.sort()
    for i in range(n - 2, math.floor(n / 2) - 1, -1):
        if sum(arr[:i]) < sum(arr[i:]):
            return arr[i:]
