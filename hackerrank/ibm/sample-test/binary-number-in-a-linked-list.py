#
# Complete the 'getNumber' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_SINGLY_LINKED_LIST binary as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def getNumber(binary):
    n = 0
    p = binary
    while p is not None:
        n += 1
        p = p.next
    s = 0
    p = binary
    for i in range(n - 1, -1, -1):
        s += p.data * 2**i
        p = p.next
    return s
