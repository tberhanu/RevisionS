"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_element(head, val):
    """
    Runtime: 72 ms, faster than 94.74% of Python3 online submissions for Remove Linked List Elements.
    """
    dummy = ListNode(-999)
    ptr = dummy
    ptr.next = head

    while ptr != None and ptr.next is not None:
        if ptr.next.val == val:
            ptr.next = ptr.next.next
        else:
            ptr = ptr.next
    return dummy.next