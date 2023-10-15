#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getScoreDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY numSeq as parameter.
#


def getScoreDifference(numSeq):
    arr = numSeq
    s1 = 0
    s2 = 0
    for i in range(len(arr)):
        n = arr[0]
        if i % 2 == 0:
            s1 += n
        else:
            s2 += n
        arr.pop(0)
        if n % 2 == 0:
            arr.reverse()
    return s1 - s2


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    numSeq_count = int(input().strip())

    numSeq = []

    for _ in range(numSeq_count):
        numSeq_item = int(input().strip())
        numSeq.append(numSeq_item)

    result = getScoreDifference(numSeq)

    fptr.write(str(result) + "\n")

    fptr.close()
