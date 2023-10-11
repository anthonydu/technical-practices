#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
import math


def findMedian(arr):
    arr.sort()
    return arr[math.floor(len(arr) / 2)]
