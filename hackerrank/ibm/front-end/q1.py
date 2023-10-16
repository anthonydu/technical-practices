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