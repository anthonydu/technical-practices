#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#


def superDigit(n, k):
    if len(n) == 1:
        return n
    s = 0
    for d in n:
        s += int(d)
    return superDigit(str(s * k), 1)
