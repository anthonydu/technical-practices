# Complete the getSequenceSum function below.
def getSequenceSum(i, j, k):
    s = 0
    s += (i + j - 1) * (j - i) / 2
    s += (j + k) * (j - k + 1) / 2
    return int(s)
