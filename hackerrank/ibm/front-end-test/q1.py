#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countFaults' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY logs
#


def countFaults(n, logs):
    counts = {}
    replacements = 0
    for i in range(len(logs)):
        log = logs[i].split()
        id = log[0]
        status = log[1]
        if status == "error":
            if id in counts:
                counts[id] += 1
            else:
                counts[id] = 1
        else:
            counts[id] = 0
        if counts[id] >= 3:
            replacements += 1
            counts[id] = 0
    return replacements


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    result = countFaults(n, logs)

    fptr.write(str(result) + "\n")

    fptr.close()
