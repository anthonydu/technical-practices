#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    sentinel = SinglyLinkedListNode(None)
    curr = sentinel
    while head1 and head2:
        if head1.data > head2.data:
            curr.next = head2
            head2 = head2.next
        else:
            curr.next = head1
            head1 = head1.next
        curr = curr.next
    if head1:
        curr.next = head1
    if head2:
        curr.next = head2
    return sentinel.next
